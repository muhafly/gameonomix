import json
import math
import numpy as np
from django.http import JsonResponse
from economies.models import *

def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]
    
def api_home(request, *args, **kwargs):
    data=None
    level=0
    habit=0
    event_read=0
    economic_model=0
    score=0
    try:
        data=json.loads(request.body)
        data=dict(data)
        if data:
            level=data['level']
            habit=data['habit']
            event_read=data['event']
            if level<1:
                level=1
            if level>30:
                level=30    
            if habit<1:
                habit=1
            if habit>10:
                habit=10
            event = Event.objects.filter(pk=event_read)[0]
            economic_model = EconomicModel.objects.filter(event=event)[0]
            scores_array = economic_model.economic_model['model']
            frac, whole = math.modf(habit)
            scorelow=scores_array[round(level)-1][math.floor(habit)-1]
            scorehigh=scores_array[round(level)-1][math.ceil(habit)-1]
            if frac==0:
                scoreaverage=scorelow
            else:
                scoreaverage=((1-frac)*scorelow)+(frac*scorehigh)
            return JsonResponse({"target score": scoreaverage,"input_level":level,"input_habit":habit,"input_event":event_read,"model":economic_model})
    except:
        pass
    
    return JsonResponse({"input_level":level,"input_habit":habit,"input_event":event_read,"model":economic_model})
