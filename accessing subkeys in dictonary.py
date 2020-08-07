students={"mohan":{"class":"V","roll no":2},"priya":{"class":"V","roll no":3}}
for key in students:
          print(key)
          for subkey in students[key]:
              print(subkey,":",students[key][subkey])
