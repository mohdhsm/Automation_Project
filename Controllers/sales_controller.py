from services.pipedrive_services import PipedriveService
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class SalesController:
    def __init__(self):
        self.service = PipedriveService()
        
    def get_all_deals(self) -> List[Dict]:
        """Get all deals from Pipedrive"""
        return self.service.get_all_deals()
        
    def get_deals_by_timeframe(self, timeframe: str) -> List[Dict]:
        """Get deals by timeframe (today/week/month)"""
        if timeframe == 'today':
            return self.service.get_deals_updated_today()
        elif timeframe == 'week':
            return self.service.get_deals_updated_this_week()
        elif timeframe == 'month':
            return self.service.get_deals_updated_this_month()
        else:
            raise ValueError("Invalid timeframe. Use 'today', 'week', or 'month'")
            
    def get_stalled_deals(self) -> List[Dict]:
        """Get deals not updated in 30+ days"""
        return self.service.get_stalled_deals()
        
    def get_inactive_deals(self) -> List[Dict]:
        """Get deals not updated in 60+ days"""
        return self.service.get_inactive_deals()
        
    def get_recently_won_deals(self) -> List[Dict]:
        """Get deals won in last 30 days"""
        return self.service.get_recently_won_deals()
        
    def get_aramco_projects(self) -> List[Dict]:
        """Get deals in Aramco Projects pipeline"""
        return self.service.get_aramco_projects()
        
    def get_deals_by_stages(self) -> List[Dict]:
        """Get deals in specific stages (Awaiting MDD/GR)"""
        return self.service.get_deals_by_stages()
        
    def get_deals_by_sales_person(self, name: str) -> List[Dict]:
        """Get deals by sales person name"""
        return self.service.get_deals_by_sales_person(name)
        
    def get_sales_summary_report(self) -> Dict:
        """Generate sales summary report"""
        all_deals = self.get_all_deals()
        recent_won = self.get_recently_won_deals()
        stalled = self.get_stalled_deals()
        aramco = self.get_aramco_projects()
        
        return {
            'total_deals': len(all_deals),
            'total_value': sum(d.get('value', 0) for d in all_deals),
            'recently_won': len(recent_won),
            'won_value': sum(d.get('value', 0) for d in recent_won),
            'stalled_deals': len(stalled),
            'aramco_projects': len(aramco)
        }
        
    def get_salesperson_report(self, name: str) -> Dict:
        """Generate detailed report for a salesperson"""
        deals = self.get_deals_by_sales_person(name)
        stalled = [d for d in deals if d in self.get_stalled_deals()]
        
        return {
            'name': name,
            'summary': {
                'total_deals': len(deals),
                'total_value': sum(d.get('value', 0) for d in deals),
                'stalled_deals': len(stalled),
                'active_deals': len(deals) - len(stalled)
            },
            'recent_deals': sorted(deals, key=lambda x: x.get('updated', ''), reverse=True)[:5],
            'stalled_deals': stalled
        }
