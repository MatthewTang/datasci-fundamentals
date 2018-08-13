import csv
import collections as coll
import sys
import webbrowser


def find_user_listings(records, user_id):
    user_listings = set()
    for row in records:
        if row[3] == user_id:
            user_listings.add(row[0])
    return user_listings


def find_fellow_travelers(records, user_listings):
    fellow_travelers = set()
    for row in records:
        if row[0] in user_listings:
            fellow_travelers.add(row[3])
    return fellow_travelers


def find_triangles_counts(records, fellow_travelers):
    triangles = []
    for row in records:
        if row[3] in fellow_travelers:
            triangles.append(row[0])
    return coll.Counter(triangles)


def return_recommendations(counts, user_listings):
    for listing in user_listings:
        if listing in counts:
            counts.pop(listing)
    return counts.most_common(5)


def main():
    data, user_id = sys.argv[1:]
    csv_file = open(data, newline='')
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    records = list(csv_reader)
    user_listings = find_user_listings(records, user_id)
    fellow_travelers = find_fellow_travelers(records, user_listings)
    counts = find_triangles_counts(records, fellow_travelers)
    recommendations = return_recommendations(counts, user_listings)
    print(recommendations)
    for rec in recommendations:
        webbrowser.open('https://www.airbnb.com/rooms/' + rec[0])


if __name__ == '__main__':
    main()
