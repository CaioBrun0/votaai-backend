from app.db.queries.poll_queries import PollQueries
from app.serializers.poll_serializers import PollSerializer

class PollService:

    def get_all_polls(self):
        try:
            votes = PollQueries.get_all()
            return {"success": True, "data": votes}
        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_poll(self, validated_data):
            try:
                poll = PollSerializer().create(validated_data)
                return {'success': True, 'data': poll}
            except Exception as e:
                return {'success': False, 'error': str(e)}