favorite_languages = {
	'jen' : ['python', 'ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell'],
    'steve' :['sql'],
    'mark' : ['ruby'],
}

#language = favorite_languages['sarah'].title()
#print (f"Sarah's favorite language is {language}.")

#for name, language in favorite_languages.items():
#    print (f"{name.title()}'s favorite language is {language.title()}")
 
#for name in favorite_languages.keys():
#    print(name.title())
 
#for language in favorite_languages. values():
#    print (language.title())

#for name in favorite_languages:
#    print(name.title())
 
#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print (f"Hi {name.title()}. ")
   
#    if name in friends:
#        language = favorite_languages[name].title()
#        print (f"\t{name.title()}, I see you love {language}! ")
        
#        if 'erin' not in favorite_languages.keys():
#            print ("Erin, please take our poll")

#for name in sorted(favorite_languages.keys()) :
#    print (f"{name.title()}, thank you for taking the poll. ")
 
#print ("The following languages have been mentioned. ") 

#for language in favorite_languages.values() :
#    print(language.title())
 
#for language in set(favorite_languages.values()) :
#    print(language.title())

#friends = ['jen', 'phil', 'mark']

#for name in favorite_languages.keys():
    
#    if name in friends:
#        print (f"thank you {name.title()} for taking the poll .")
#    else:
#        print (f"please {name.title()} take the poll .")

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print (f"\n{name.title()}'s favorite languages are: ")
        for language in languages: 
            print (f"\t{language.title()}")
    else:   
        language = languages
        print (f"\n{name.title()}'s favorite language is :{language.title()}")
        
        
        
        
