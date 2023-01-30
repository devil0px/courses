
from rest_framework import serilizers
from .models import Courses


class coursesSerilizers(serilizers.ModelSerilizes):

    class Meta:
        model =Courses
        fields ='__all__'

