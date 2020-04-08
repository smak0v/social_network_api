from django.utils import dateparse, timezone
from posts.models import PostLike
from rest_framework import status
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.views import APIView


class AnalyticsView(APIView):
    def get(self, request, *args, **kwargs):
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)

        df, dt = self.__validate(date_from, date_to)
        dt += timezone.timedelta(days=1)

        return Response(self.__get_response(df, dt), status=status.HTTP_200_OK)

    def __get_response(self, df, dt):
        response = {}
        post_likes = PostLike.objects.filter(timestamp__range=(df, dt))

        for i in range((dt - df).days):
            day = df + timezone.timedelta(days=i)
            response[str(day)] = 0

        for post_like in post_likes:
            response[str(post_like.timestamp.date())] += 1

        return response

    def __validate(self, date_from=None, date_to=None):
        if not date_from:
            raise ValidationError({'date_from': 'Required query param'})

        if not date_to:
            raise ValidationError({'date_to': 'Required query param', })

        df = dateparse.parse_date(date_from)
        dt = dateparse.parse_date(date_to)

        if not df or not dt:
            raise ValidationError({'error': 'At least one of the query params is not a date', })

        if df > dt:
            raise ValidationError({'date_to': 'Can not be less than date_from'})

        return df, dt
