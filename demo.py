from devXliff import XLIFF

obj = XLIFF.XLIFF("sample.txt", 'hi', 'en', True) 
#argument1: name of source text file, 
#argument2: language code for source language
#argument3: language code for target language
#argument4: specifies weather the source, target pairs have been approved or not (by default False)

#See https://www.loc.gov/standards/iso639-2/php/code_list.php to find code of a specific language


#Suppose we have a list of source text and target text and we want to save them as XLIFF file so that
#they can be used by a CAT tool. This can be achieved as follows using devXliff
list_source=["वह एक अच्छी बेटी है", "मुझे बीकानेर बहुत पसंद है", "अजमेर खूबसूरत अरावली रेंज से घिरा हुआ है"]
list_target=["She is a good daughter", "I love Bikaner", "Ajmer is surrounded by the beautiful Aravali Range"]

l = list(zip(list_source, list_target)) 
[obj.add_trans_unit(s,t) for s,t in (l)]  

xliff = obj.get_str()
with open("sample_XLIFF.xlf", "w", encoding="utf8") as f:
    f.write(xliff)