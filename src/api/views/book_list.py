
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.book.documents import BookDocument
from api.serializer.book_serializer import BookListSeralizers
# Create your views here.


class BookView(APIView):
    
    def get(self, requets):
        search_parm = self.request.GET.get("search")
        response_data = []
        if search_parm:
            books = BookDocument.search(index='books').query(
                'match',
                name={
                    "query": search_parm,
                    "minimum_should_match": "50%",
                    "fuzziness": "AUTO"   # typo ruxsat beradi
                }
            )
            response = books.execute()
            books_data = [hit.to_dict() for hit in response.hits]
            response_data = BookListSeralizers(books_data, many=True).data
        return Response({
            "message": "ok",
            "search_by": search_parm,
            "results": response_data
        })
        