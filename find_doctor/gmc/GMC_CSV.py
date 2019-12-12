import re,datetime,sys
from unidecode import unidecode
import json,requests,urllib.parse
from bs4 import BeautifulSoup
try:
    from packages.content_crawler import bot
except:
    sys.path.insert(0,'../')
    from packages.content_crawler import bot




URL="https://www.gmc.com"
robot = bot(URL)
urls=["https://www.gmc.com/previous-year/vehicles","https://www.gmc.com/current-vehicles"]
for cont_url in urls:
    (soup,code) = robot.get_content(cont_url,{"method":"get","bs4":"y"})
    product_link=soup.find_all("h2",{"class":"q-display3"})
    for link in product_link:
        product_link=URL+link.find("a").get("href")
        print(product_link)
# sub=soup.find("ul",{"role":"tablist"}).find_all("div",{"class":"nav-copy"})
# nav_tab=soup.find("div",{"class":"dropdown-wholegoods__content"}).find("div",{"class":"tab-content"}).find_all("a",{"class":"display-block"})
# for nav in nav_tab:
#     product_url="https://atv.polaris.com" + nav.get("href")
#     (pagcont,code) = robot.get_content(product_url,{"method":"get","bs4":"y"})
#     mod_cont=pagcont.find_all("dl",{"class":"accordion-simple__container"})
    

#     for mod,sb in zip(mod_cont,sub):
#         model_id=mod.find("h3").text
#         # print(model_id)
#         subcat=sb.text
#         feats=[]
#         option=[]
#         all_imges=[]

#         desc=model_id+params["ManufacturerName"]
    

#         msrp=mod.find("span",{"class":"wholegood-price font-size-md font-weight-bold"}).text
#         try:
#             feats1=mod.find("div",{"class":"description list-style--disc-inside"}).find_all("li")
#             for fe in feats1:
#                 feats.append(fe.text)

#         except:
#             pass

#         try:
#             decs=pagcont.find("div",{"role":"definition"}).text
         

#         except:
#             pass

#         try:
#             fet=pagcont.find("section",{"id":"features"}).find_all("section")
#             for fe in fet:
                
#                 try:
#                     imgs=fe.find("div",{"class":"img-background-container"}).find("img").get("srcset").split("?")[0]
#                     all_imges.append(imgs)
                   
#                 except:
#                     pass

#                 try:
#                     feat_img_text=fe.find("div",{"class":"copy-generic__description font-color-light"}).text
#                     feats.append(feat_img_text.strip())
#                 except:
#                     pass

#         except:
#             pass

#         try:
#             nav_link=pagcont.find("a",{"data-layer-label":"View All Specs"}).get("href")
#             spec_link="https://atv.polaris.com" + nav_link
#             (spcont,code) = robot.get_content(spec_link,{"method":"get","bs4":"y"})
#             spec=spcont.find("div",{"class":"specs-full__specs mobile-margin-top-sm"}).find_all("div",{"class":"specs-full__spec padding-xs"})
#             for sp in spec:
#                 specname=sp.find("div",{"role":"rowheader"}).text
#                 specvalue=sp.find("div",{"role":"gridcell"}).text
#                 if(re.search(r'(?i)N/A|Not Equipped',specvalue)):
#                     pass
#                 else:
#                     if len(specvalue)>1:
#                         if(re.search(r'(?i)ENGINE|Cooling|Cylinders Displacement|Drive|Horsepower|Transmission/Final Drive',specname)):
#                             robot.creat_spec({"specNamel":specname,"metricUnitValue":specvalue},"engine") 
#                         elif(re.search(r'OPERAT|Capacity|LP Tank|Water Tank|Gray Water Tank|Fresh Water Tank|Black Water Tank',specname)):
#                             robot.creat_spec({"specNamel":specname,"metricUnitValue":specvalue},"operation")
#                         elif(re.search(r'(?i)Exterior height|Height|Floor Length|Exterior Height|Exterior Length|Exterior Width|Wheel Well|Center of Gravity|Wheelbase|Front Tires|Overall Vehicle Size',specname)):
#                             robot.creat_spec({"specNamel":specname,"metricUnitValue":specvalue},"measurements")
#                         elif(re.search(r'(?i)weight|Hitch Weight|GVWR|UVW|CCC|Ship Weight|Estimated Dry Weight',specname)):
#                             robot.creat_spec({"specNamel":specname,"metricUnitValue":specvalue},"weights")
#                         else:
#                             robot.creat_spec({"specNamel":specname,"metricUnitValue":specvalue},"others" )   

#         except:
#             pass

#         try:
#             galry=product_url+ "gallery"
#             (galcont,code) = robot.get_content(galry,{"method":"get","bs4":"y"})
#             imgsrc=galcont.find("section",{"id":"model-gallery-container"}).find_all("img")
#             for imge in imgsrc:
#                 src=imge.get("src").split("?v")[0]
#                 all_imges.append(src)

            

#         except:
#             pass

        
#         temp_fe=set(feats)
#         for f in temp_fe:
#             robot.Features(f)
#         temp_op=set(option)
#         for o in temp_op:
#             robot.Options(o)
#         tem_imp=set(all_imges)
#         for im in tem_imp:
#             robot.fetch_img_manual(im)
            
        
#         robot.ObjectID(model_id)
#         robot.ProductUrl(product_url)
#         robot.Description(desc)
#         robot.SubCategory(subcat)
#         robot.MasterCategory(category)
#         robot.Country("US")
#         robot.ManufacturerName("Polaris")       
#         robot.make_json()
# robot.destroy()
