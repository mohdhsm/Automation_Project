import requests
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class PipedriveService:
    def __init__(self):
        self.api_token = "15c3e2fb8501a925f71db8de534f3bed42345041"
        self.base_url = "https://api.pipedrive.com/v1"
        self.session = requests.Session()

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> List[Dict]:
        """Base method for making API requests"""
        params = params or {}
        params['api_token'] = self.api_token
        
        try:
            response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            data = response.json()
            return data.get('data', [])
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            return []

    def _normalize_deal(self, deal: Dict) -> Dict:
        """Normalize deal data structure"""
        return {
            'id': deal.get('id'),
            'title': deal.get('title'),
            'value': deal.get('value'),
            'status': deal.get('status'),
            'stage_id': deal.get('stage_id'),
            'person_id': deal.get('person_id'),
            'org_id': deal.get('org_id'),
            'owner_id': deal.get('user_id'),
            'created': deal.get('add_time'),
            'updated': deal.get('update_time')
        }

    def get_all_deals(self) -> List[Dict]:
        """Get all deals from Pipedrive"""
        return [self._normalize_deal(deal) for deal in self._make_request('deals')]

    def get_all_persons(self) -> List[Dict]:
        """Get all persons from Pipedrive"""
        return self._make_request('persons')

    def _get_deals_by_timeframe(self, timeframe: str) -> List[Dict]:
        """Helper method for time-based deal queries"""
        today = datetime.now().date()
        params = {}
        
        if timeframe == 'today':
            params['filter_id'] = 'today'
        elif timeframe == 'week':
            params['start_date'] = (today - timedelta(days=today.weekday())).isoformat()
            params['end_date'] = today.isoformat()
        elif timeframe == 'month':
            params['start_date'] = today.replace(day=1).isoformat()
            params['end_date'] = today.isoformat()
        
        deals = self._make_request('deals', params)
        return [self._normalize_deal(deal) for deal in deals]

    def get_deals_updated_today(self) -> List[Dict]:
        """Get deals updated today"""
        return self._get_deals_by_timeframe('today')

    def get_deals_updated_this_week(self) -> List[Dict]:
        """Get deals updated this week"""
        return self._get_deals_by_timeframe('week')

    def get_deals_updated_this_month(self) -> List[Dict]:
        """Get deals updated this month"""
        return self._get_deals_by_timeframe('month')

    def get_stalled_deals(self) -> List[Dict]:
        """Get deals not updated in over 30 days"""
        cutoff = (datetime.now() - timedelta(days=30)).date().isoformat()
        deals = self._make_request('deals', {'filter_id': 'all_not_updated', 'start_date': cutoff})
        return [self._normalize_deal(deal) for deal in deals]

    def get_deals_by_sales_person(self, name: str) -> List[Dict]:
        """Get open deals by sales person name"""
        users = self._make_request('users', {'term': name})
        if not users:
            return []
            
        user_id = users[0].get('id')
        deals = self._make_request('deals', {'user_id': user_id, 'status': 'open'})
        return [self._normalize_deal(deal) for deal in deals]

    def get_inactive_deals(self) -> List[Dict]:
        """Get deals not updated in last 60 days"""
        cutoff = (datetime.now() - timedelta(days=60)).date().isoformat()
        deals = self._make_request('deals', {'filter_id': 'all_not_updated', 'start_date': cutoff})
        return [self._normalize_deal(deal) for deal in deals]

    def get_recently_won_deals(self) -> List[Dict]:
        """Get deals won in last 30 days"""
        cutoff = (datetime.now() - timedelta(days=30)).date().isoformat()
        deals = self._make_request('deals', {'status': 'won', 'start_date': cutoff})
        return [self._normalize_deal(deal) for deal in deals]

    def get_aramco_projects(self) -> List[Dict]:
        """Get deals in 'Aramco Projects' pipeline"""
        pipelines = self._make_request('pipelines', {'term': 'Aramco Projects'})
        if not pipelines:
            return []
            
        pipeline_id = pipelines[0].get('id')
        deals = self._make_request('deals', {'pipeline_id': pipeline_id})
        return [self._normalize_deal(deal) for deal in deals]

    def get_deals_by_stages(self) -> List[Dict]:
        """Get deals in specific stages"""
        stage_names = ["Awaiting MDD", "Awaiting GR", "UNDERPROGRESS"]
        all_stages = self._make_request('stages')
        stage_ids = [s['id'] for s in all_stages if s.get('name') in stage_names]
        
        if not stage_ids:
            return []
            
        deals = []
        for stage_id in stage_ids:
            deals.extend(self._make_request('deals', {'stage_id': stage_id}))
            
        return [self._normalize_deal(deal) for deal in deals]

    def get_new_deals_by_timeframe(self, timeframe: str) -> List[Dict]:
        """Helper method for new deal time queries"""
        today = datetime.now().date()
        params = {}
        
        if timeframe == 'today':
            params['filter_id'] = 'today'
        elif timeframe == 'week':
            params['start_date'] = (today - timedelta(days=today.weekday())).isoformat()
            params['end_date'] = today.isoformat()
        elif timeframe == 'month':
            params['start_date'] = today.replace(day=1).isoformat()
            params['end_date'] = today.isoformat()
        
        deals = self._make_request('deals', params)
        return [self._normalize_deal(deal) for deal in deals]

    def get_new_deals_today(self) -> List[Dict]:
        """Get new deals created today"""
        return self.get_new_deals_by_timeframe('today')

    def get_new_deals_this_week(self) -> List[Dict]:
        """Get new deals created this week"""
        return self.get_new_deals_by_timeframe('week')

    def get_new_deals_this_month(self) -> List[Dict]:
        """Get new deals created this month"""
        return self.get_new_deals_by_timeframe('month')

"""
Pipedrive API Service

This class is responsible for making API calls to Pipedrive and retrieving data.
It only gets data from Pipedrive and does not send any data to it.

The class methods retrieve data in JSON format and normalize it for easier use.

Implemented API calls:
1. Get all deals
2. Get all persons
3. Get deals updated today
4. Get deals updated this week
5. Get deals updated this month
6. Get stalled deals (not updated in over 30 days)
7. Get open deals by sales person name
8. Get inactive deals (not updated in 60 days)
9. Get recently won deals (last 30 days)
10. Get deals in 'Aramco Projects' pipeline
11. Get deals in specific stages
12. Get new deals created this week
13. Get new deals created this month
14. Get new deals created today
"""
