from .models import HXLData, IATIData, ShelterData
import hxl
import iati
import csv
import requests


class UpdateDB():
    
    def updateShelter(self):
        csvShelterFileLocation = '/Users/dp/Documents/LiClipseWorkspace/IATIHDXAPINepal/data/shelterCluser_NP_simplified_single.csv'
        with open(csvShelterFileLocation, 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader)
            for row in spamreader:
                toSave = ShelterData()
                toSave.district = row[0]
                try:
                    toSave.blankets = int(row[1])
                except ValueError: pass
                try:
                    toSave.cgi = int(row[5])
                except ValueError: pass
                try:
                    toSave.clothes = int(row[6])
                except ValueError: pass
                try:
                    toSave.kitchenSets = int(row[15])
                except ValueError: pass
                try:
                    toSave.tarpaulin = int(row[26])
                except ValueError: pass
                try:
                    toSave.tents = int(row[28])
                except ValueError: pass    
                
                toSave.save()
        return
    
    def updateIATI(self):
        iatiFileLocation = '/Users/dp/Documents/LiClipseWorkspace/IATIHDXAPINepal/data/iati-datastore_NP_72010_wo_result_query.xml'
        with open(iatiFileLocation, 'rt', encoding='utf-8') as xml_file_object:
            dataset_as_string = xml_file_object.read()
        dataset = iati.Dataset(dataset_as_string)  
        listIATIIActivities = dataset.xml_tree.xpath('iati-activity')
        for iatiActivity in listIATIIActivities:
            toSave = IATIData()        
            try: 
                toSave.iatiId = iatiActivity.xpath('iati-identifier/text()')[0]
            except IndexError: pass
            try: 
                toSave.reportingOrg = iatiActivity.xpath('reporting-org/narrative/text()')[0]
            except IndexError: pass
            try: 
                toSave.title = iatiActivity.xpath('title/narrative/text()')[0]
            except IndexError: pass
            try: 
                toSave.telephone = iatiActivity.xpath('contact-info/telephone/text()')[0]
            except IndexError: pass
            try: 
                toSave.email = iatiActivity.xpath('contact-info/email/text()')[0]
            except IndexError: pass
            try: 
                toSave.website = iatiActivity.xpath('contact-info/website/text()')[0]
            except IndexError: pass
            
            toSave.save()  
        return
    
    def updateIATIFromRemote(self):
        iatiFileLocation = 'http://datastore.iatistandard.org/api/1/access/activity.xml?recipient-country=NP&sector=72010&limit=200'
        resp = requests.get(iatiFileLocation)
        dataset = iati.Dataset(resp.content)
        listIATIIActivities = dataset.xml_tree.xpath('iati-activities/iati-activity')
        for iatiActivity in listIATIIActivities:
            toSave = IATIData()
            try: 
                toSave.iatiId = iatiActivity.xpath('iati-identifier/text()')[0]
            except IndexError: pass
            try: 
                toSave.reportingOrg = iatiActivity.xpath('reporting-org/narrative/text()')[0]
            except IndexError: pass
            try: 
                toSave.title = iatiActivity.xpath('title/narrative/text()')[0]
            except IndexError: pass
            try: 
                toSave.telephone = iatiActivity.xpath('contact-info/telephone/text()')[0]
            except IndexError: pass
            try: 
                toSave.email = iatiActivity.xpath('contact-info/email/text()')[0]
            except IndexError: pass
            try: 
                toSave.website = iatiActivity.xpath('contact-info/website/text()')[0]
            except IndexError: pass
            
            toSave.save()  

        return
    
    def updateHXL(self):
        hxlFileLocation = '/Users/dp/Documents/LiClipseWorkspace/IATIHDXAPINepal/data/hxl_np_population,dead,injured,houses2.csv'
        result = hxl.data(hxlFileLocation, allow_local=True)
        for row in result:
            toSave = HXLData()                        
            toSave.district = format(row.get('#adm2'))
            toSave.population = format(row.get('#population+num'))            
            toSave.peopleInjured = format(row.get('#affected+injured+num'))            
            toSave.femalesDead = format(row.get('#affected+dead+f+num'))
            toSave.malesDead = format(row.get('#affected+dead+m+num'))            
            toSave.housesDamaged = format(row.get('#damaged+houses+num'))
            toSave.housesDestroyed = format(row.get('#destroyed+houses+num'))            
            toSave.save()
        return
    
    
    
    
    
    
    
