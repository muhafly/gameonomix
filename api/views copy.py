from rest_framework.response import Response
from rest_framework import views, viewsets, status
from . import serializers
from . import Score

scores = {
    1: Score(level=10, habit=10, score=100),
    2: Score(level=10, habit=20, score=200),
}

def get_next_score_id():
    return max(scores) + 1


class ScoreViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.ScoreSerializer

    def list(self, request):
        serializer = serializers.ScoreSerializer(
            instance=scores.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.ScoreSerializer(data=request.data)
        if serializer.is_valid():
            score = serializer.save()
            score.id = get_next_score_id()
            scores[score.id] = score
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            score = scores[int(pk)]
        except KeyError:
            return Response(status=score.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=score.HTTP_400_BAD_REQUEST)

        serializer = serializers.ScoreSerializer(instance=score)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            score = scores[int(pk)]
        except KeyError:
            return Response(score=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(score=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.ScoreSerializer(
            data=request.data, instance=score)
        if serializer.is_valid():
            score = serializer.save()
            scores[score.id] = score
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            score = scores[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.ScoreSerializer(
            data=request.data,
            instance=score,
            partial=True)
        if serializer.is_valid():
            score = serializer.save()
            scores[score.id] = score
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            score = scores[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del scores[score.id]
        return Response(status=status.HTTP_204_NO_CONTENT)