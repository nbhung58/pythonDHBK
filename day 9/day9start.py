programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Function"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary = { }
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary
for thing in programming_dictionary:
  print(thing)
  print(programming_dictionary[thing])

  #Nesting
capitals = {
  "France" : "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", 'Hamburg', "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cites_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": ["Berlin", 'Hamburg', "Stuttgart"],
}

#Nesting Dictionary in a list
travel_log =[ 
  {
    "country": "France", 
    "cites_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", 'Hamburg', "Stuttgart"],
    "total visis": 5
  },
]