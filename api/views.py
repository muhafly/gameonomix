import json
import math
import numpy as np
from django.http import JsonResponse
level_array = [1,2,3,4,5]
habit_array = [1,2,3,4,5]
scores_array=[[1,2,3,4,5],[2,4,5,8,10],[3,6,9,12,15],[4,8,12,16,20],[5,10,15,20,25]]
def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]
    
def api_home(request, *args, **kwargs):
    data=None
    score=0
    try:
        data=json.loads(request.body)
        data=dict(data)
        if data:
            level=data['level']
            habit=data['habit']
            score=scores_array[level-1][habit-1]
            return JsonResponse({"target score": score})
    except:
        pass
    
    return JsonResponse({"message":"This is the the amazing gameonomics platform. Please provied a level and a habit in json format to get the target score!"})
