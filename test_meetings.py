#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime, timedelta
from models.meeting import Meeting
from Controllers.meeting_controller import MeetingController
from views.meeting_view import MeetingView

def main():
    # Create controller and view
    controller = MeetingController()
    view = MeetingView()

    # Create sample meetings
    meeting1 = Meeting(
        meeting_type="one_on_one",
        date=datetime.now() + timedelta(days=1),
        summary="Weekly 1:1 with manager",
        participants=[uuid4()]
    )
    
    meeting2 = Meeting(
        meeting_type="group",
        date=datetime.now() + timedelta(days=3),
        summary="Team sprint planning",
        participants=[uuid4(), uuid4(), uuid4()]
    )

    # Test create
    created1 = controller.create_meeting(meeting1)
    created2 = controller.create_meeting(meeting2)
    print(f"Created meetings: {created1.id}, {created2.id}")

    # Test get all
    all_meetings = controller.get_all_meetings()
    print(f"\nAll meetings ({len(all_meetings)}):")
    view.display_meetings(all_meetings)

    # Test get single
    single_meeting = controller.get_meeting(created1.id)
    print("\nSingle meeting details:")
    view.display_meeting(single_meeting)

    # Test update
    updated = controller.update_meeting(created2.id, {
        "summary": "URGENT: Team sprint planning",
        "meeting_type": "emergency"
    })
    print("\nAfter update:")
    view.display_meeting(updated)

    # Test delete
    deleted = controller.delete_meeting(created1.id)
    print(f"\nDeleted meeting {created1.id}: {deleted}")

    # Verify deletion
    remaining = controller.get_all_meetings()
    print(f"\nRemaining meetings ({len(remaining)}):")
    view.display_meetings(remaining)

if __name__ == "__main__":
    main()
