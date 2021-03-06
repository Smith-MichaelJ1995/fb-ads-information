import json
results = json.load(open('results.json', 'r'))
remaining = json.load(open('remaining.json', 'r'))

# remove advertisers we've already processed
deletedAdvertisers = []

# create placeholder for target keywords
keywords = {
    "Home-Repair": [],
    "Health": ["Medicine", "Wellness"],
    "Food-Beverage": [],
    "Software": [],
    "Financial": [],
    "Merchandise": [
       "The 12ish Style",
       "The Bar Method",
       "The Beautiful Circus",
       "The Beliveau Group of EXP Realty",
       "THE COLLECTION",
       "The Coloradoan",
       "The Commercial Appeal",
       "The Dental Lounge",
       "The Des Moines Register",
       "The Dodo",
       "The Drop, exclusive to Amazon",
       "The Excellence Collection",
       "The FM Test",
       "The Fund for American Studies (TFAS)",
       "The Gardens at Winsted Skilled Nursing & Assisted Living",
       "The Good Fight",
       "The Greens at Pinehurst Rehabilitation & Living Center",
       "The Groves",
       "The Healey Pre-Owned Network",
       "The Heritage Foundation",
       "The Home Depot",
       "The Jackson Hive",
       "The Leukemia & Lymphoma Society",
       "the love designed life",
       "The Mortgageman",
       "The Niello Company",
       "The North Face",
       "The Novak Team at Keller Williams PNW",
       "The Post-Crescent (Appleton-Fox Cities, Wisconsin)",
       "The Reeds at Shelter Haven",
       "The River's Edge of Oakmont",
       "The Seeing Eye, Inc.",
       "The Suburban Collection",
       "The Superhero Teacher's Resources",
       "The Sweet Mama Life.",
       "The True Spoon",
       "The Voter Participation Center",
       "The Waterview Woods",
       "The Woodlands Hills",
    ],
    "Insurance": [],
    "Interest-Group": [],
    "Entertainment": ["Gossip"],
    "Auto-Retail": []
}

def filterIntoBucket(advertiser):

    # CHECK "Home-Repair"
    for word in keywords["Home-Repair"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to home-repair section 
            results["Home-Repair"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Home-Repair'".format(advertiser))
            return

    # CHECK "Health"
    for word in keywords["Health"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to health section 
            results["Health"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Health'".format(advertiser))
            return

    # CHECK "Food-Beverage"
    for word in keywords["Food-Beverage"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to food-bev section 
            results["Food-Beverage"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Food-Bev'".format(advertiser))
            return

    # CHECK "Software"
    for word in keywords["Software"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to software section 
            results["Software"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Software'".format(advertiser))
            return

    # CHECK "Financial"
    for word in keywords["Financial"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to Financial section 
            results["Financial"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Financial'".format(advertiser))
            return
    
    # CHECK "Merchandise"
    for word in keywords["Merchandise"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to merchandise section 
            results["Merchandise"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Merchandise'".format(advertiser))
            return

    # CHECK "Insurance"
    for word in keywords["Insurance"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to Insurance section 
            results["Insurance"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Insurance'".format(advertiser))
            return

    # CHECK "Interest-Group"
    for word in keywords["Interest-Group"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to Entertainment section 
            results["Interest-Group"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Interest-Group'".format(advertiser))
            return
    
    # CHECK "Entertainment"
    for word in keywords["Entertainment"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to Entertainment section 
            results["Entertainment"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Entertainment'".format(advertiser))
            return
    
    # CHECK "Auto-Retail"
    for word in keywords["Auto-Retail"]:

        # determine if advertiser is of type auto
        if word.lower() in advertiser.lower(): 

            # append result to cars section 
            results["Auto-Retail"].append(advertiser)
            deletedAdvertisers.append(advertiser)
            print("{} Sorted Into 'Auto-Retail'".format(advertiser))
            return

runningTotal = 0

# traverse through all records
for category in results.keys():
    
    # traverse through all results
    categoryTotal = len(results[category])

    print("Total For Category '{}': {}".format(category, categoryTotal))
    runningTotal += categoryTotal

# process all remaining advertisers
# for advertiser in remaining:

#     # pass into filterBucket Function
#     filterIntoBucket(advertiser)


print("Total Advertisers Accounted For = {}".format((runningTotal)))
print("Total Remaining Advertisers = {}".format(len(remaining)))

# FINAL (ABRIGDED) COUNTS:
# 'Home-Repair': 36  36/371 = 0.09; (0.09 x 853) = 77; 77 + 36 = 113
# 'Health': 94   94/371 = 0.25; (0.25 x 853) = 216; 216 + 94 = 310
# 'Food-Beverage': 35   35/371 = (0.09 x 853) = 77; 77 + 35 =  112
# 'Software': 33    33/371 = (0.09 x 853) = 77; 77 + 33 = 111
# 'Financial': 31   31/371 = (0.08 x 853) = 68; 68 + 31 = 99
# 'Merchandise': 69  69/371 = (0.18 x 853) = 158; 158 + 69 = 227
# 'Insurance': 5    5/371 = (0.01 x 853) = 12; 5 + 12 = 17
# 'Interest-Group': 29   29/371 = (0.07 x 853) = 67; 67 + 29 = 96
# 'Entertainment': 39   39/371 = (0.10 x 853) = 86; 86 + 39 = 125 
# 'Auto-Retail': 2000
#Total Advertisers Accounted For = 2371
#Total Remaining Advertisers = 853

'Home-Repair': 113
'Health': 310
'Food-Beverage': 112
'Software': 111
'Financial': 99
'Merchandise': 227
'Insurance': 17
'Interest-Group': 96
'Entertainment': 125
'Auto-Retail': 2000
#Results = 3210

# FB Advertisers [113] Home Repair
# FB Advertisers [310] Health
# FB Advertisers [112] Food-Beverage
# FB Advertisers [111] Software
# FB Advertisers [99] Financial
# FB Advertisers [227] Merchandise
# FB Advertisers [17] Insurance
# FB Advertisers [96] Interest-Group
# FB Advertisers [125] Entertainment
# FB Advertisers [2000] Auto-Retail



# show remaining advertisers before
#print("Advertisers Before: {}".format(len(remaining)))

# scratch all advertisers from results
#for deletedAdvertiser in deletedAdvertisers:
#   remaining.remove(deletedAdvertiser)

# show remaining advertisers after
# print("Advertisers After: {}".format(len(remaining)))

# write file to filesyste,
# with open('results.json', 'w') as convert_file: 
#   convert_file.write(json.dumps(results, indent=3))

# write file to filesyste,
# with open('remaining.json', 'w') as convert_file: 
#    convert_file.write(json.dumps(remaining, indent=3))


# SCRIPT DATA
# ' Type a list of Flows between Nodes, like:
# '     Source [AMOUNT] Target
# ' Examples:
# ' Primary Data
# FB Advertisers [113] Home Repair
# FB Advertisers [310] Health
# FB Advertisers [112] Food-Beverage
# FB Advertisers [111] Software
# FB Advertisers [99] Financial
# FB Advertisers [227] Merchandise
# FB Advertisers [17] Insurance
# FB Advertisers [96] Interest-Group
# FB Advertisers [125] Entertainment
# FB Advertisers [2000] Auto-Retail

# ' Yes/No/LOL
# Home Repair [33] Yes
# Home Repair [90] No

# ' You can set a specific color for a Node:
# :Taxes #CC66FF
# '                                    ...and for a Flow:
# ' Budget [160] Other Necessities #00CC00
# ' Visit the 'Manual' link for more!

# ' After entering your data, use the
# ' controls below to customize your
# ' diagram's appearance.