import json
results = json.load(open('results.json', 'r'))
remaining = json.load(open('remaining.json', 'r'))

# remove advertisers we've already processed
deletedAdvertisers = []

# create placeholder for target keywords
keywords = {
    "Home-Repair": [],
    "Health": ["Chiro"],
    "Food-Beverage": [],
    "Software": [],
    "Merchandise": [],
    "Insurance": [],
    "Interest-Group": [],
    "Entertainment": [],
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


# traverse through all records
for advertiser in remaining:
    
    # pass into filterBucket Function
    filterIntoBucket(advertiser)


# show remaining advertisers before
print("Advertisers Before: {}".format(len(remaining)))

# scratch all advertisers from results
for deletedAdvertiser in deletedAdvertisers:
    remaining.remove(deletedAdvertiser)

# show remaining advertisers after
print("Advertisers After: {}".format(len(remaining)))

# write file to filesyste,
with open('results.json', 'w') as convert_file: 
    convert_file.write(json.dumps(results))

# write file to filesyste,
with open('remaining.json', 'w') as convert_file: 
    convert_file.write(json.dumps(remaining))

