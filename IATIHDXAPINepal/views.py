from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  HXLData, IATIData, ShelterData
from .serializers import   HXLTestSerializer, IATITestSerializer, ShelterItemsTestSerializer
from .update import UpdateDB
from rest_framework.generics import ListCreateAPIView
from rest_framework import filters
import operator


# hxl/{district}
class HXLQuery(ListCreateAPIView):

    model = HXLData
    serializer_class = HXLTestSerializer
    filter_backends = (filters.OrderingFilter,)
    
    def get_queryset(self):
        queryset = HXLData.objects.all()        
        queryDistrict = self.request.query_params.get('district', None)
        if queryDistrict is not None:
            queryset = queryset.filter(district=queryDistrict)
        
        return queryset

# updatehxl/
class UpdateHXL(APIView):
    
    def get(self, request):
        hxlData = HXLData.objects.all()
        serializer = HXLTestSerializer(hxlData, many=True)                
        
        UpdateDB().updateHXL()
        
        return Response(serializer.data)
    
    def post(self):
        pass

# updateiati/
class UpdateIATI(APIView):
    
    def get(self, request):
        UpdateDB().updateIATI()
        
        iatiData = IATIData.objects.all()
        serializer = IATITestSerializer(iatiData, many=True)                
        
        return Response(serializer.data)
    
    def post(self):
        pass  
   

# shelter/
class ShelterQuery(ListCreateAPIView):
    
    shelterData = ShelterData
    serializer_class = ShelterItemsTestSerializer
    filter_backends = (filters.OrderingFilter,)
    
    def get_queryset(self):
        
        queryset = ShelterData.objects.all()
        queryDistrict = self.request.query_params.get('district', None)
        if queryDistrict is not None:
            queryset = queryset.filter(district=queryDistrict)
        
        return queryset
    
    def post(self):
        pass

# updateShelter/
class UpdateShelter(APIView):
    
    def get(self, request):
        UpdateDB().updateShelter()
        
        shelterData = ShelterData.objects.all()
        serializer = ShelterItemsTestSerializer(shelterData, many=True)
        
        return Response(serializer.data)
    
    def post(self):
        pass

# multitest/
class MultiHXLandShelterView(APIView):
    
    filter_backends = (filters.OrderingFilter,)
    
    def get(self, request, format=None, **kwargs):
        shelterData = ShelterData.objects.all()
        hxlData = HXLData.objects.all()
        shelter_serializer = ShelterItemsTestSerializer(shelterData, many=True)
        hxl_serializer = HXLTestSerializer(hxlData, many=True)
        
        shelterList = []
        hxlList = []
                
        # iterate through shelter list
        for shelterEntry in shelter_serializer.data:
            # check for 'district' name in shelter entry
            districtShelter = shelterEntry['district']
            # iterate through hxl list
            for hxlEntry in hxl_serializer.data:
                # if shelter district matches hxl district i.e. a district is found in both lists, hxl and shelter                
                if districtShelter == hxlEntry['district']:
                    shelterList.append(shelterEntry)
                    hxlList.append(hxlEntry)
        
        # Sort both lists by district and merge them into shelterList
        sorting_key = operator.itemgetter('district')
        shelterList = sorted(shelterList, key=sorting_key)
        hxlList = sorted(hxlList, key=sorting_key)
        for i, j in zip(shelterList, hxlList):
            i.update(j)
           
        return Response(shelterList)
        
        """
        return Response({
            'shelter': shelter_serializer.data,
            'hxl': hxl_serializer.data,
        })
        """
  
    def post(self):
        pass  
  

# iati/
class IATIQuery(ListCreateAPIView):

    #iatiData = IATIData
    serializer_class = IATITestSerializer
    
    
    def get_queryset(self):
        
        queryset = IATIData.objects.all()        
        
        queryReportingOrg = self.request.query_params.get('reporting-org', None)
        if queryReportingOrg is not None:
            queryset = queryset.filter(reportingOrg=queryReportingOrg)
        
        querySearch = self.request.query_params.get('search', None)
        if querySearch is not None:
            queryset = queryset.filter(title__icontains=querySearch)
        
        queryTitle = self.request.query_params.get('title', None)
        if queryTitle is not None:
            queryset = queryset.filter(title=queryTitle)        
        
        queryTitle = self.request.query_params.get('remote', None)
        if queryTitle is not None:
            UpdateDB().updateIATIFromRemote() 
        
        
        return queryset
 
    def post(self):
        pass
    
    
    
    
    
    