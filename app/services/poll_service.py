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
        

    def get_poll_by_id(self,id):

        try:
            poll = PollQueries.get_by_id(id)
            return {"success": True, "data": poll}
        
        except Exception as e:
            return {"success": False, "error": str(e)}


    def get_poll_by_title(self,order, category, title):
        try:
            if order == 'old' :
                poll = PollQueries.get_where('title','criation_date','ASC', category, title)
            elif order == 'new':
                poll = PollQueries.get_where('title','criation_date','DESC', category,title)
            return {"success": True, "data": poll}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_poll_by_tag(self, order, category, tag):
        try:
            if order == 'old':
                poll = PollQueries.get_where('tags', 'criation_date','ASC', category, tag)
            elif order == 'new':
                poll = PollQueries.get_where('tags', 'criation_date','DESC', category, tag)
            return {"success": True, "data": poll}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_poll_by_code(self, code):
        try:
            poll = PollQueries.get_where('code','','','',code)
            return {"success": True, "data": poll}
        except Exception as e:
            return {"success": False, "error": str(e)}
