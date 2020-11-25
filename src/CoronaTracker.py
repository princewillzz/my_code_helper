import requests
from .speaker import Speaker


class CoronaTracker:

    # Create some properties of the class
    brokenAPIFlag = True

    HOME_URL = "https://covid19.mathdro.id/api"
    COUNTRY_SPECIFIC_UPDATE_URL = "https://covid19.mathdro.id/api/countries/"

    confirmed_until_today = None
    recovered_until_today = None
    deaths_until_today = None
    lastUpdatedTime = None

    speaker = None

    # Initialize the object and check if everything is working fine or not
    def __init__(self):

        try:
            self.initialize()
            self.brokenAPIFlag = False

        except Exception as e:
            print("Unable to connect...Check your Internet connection")
            print("Try again later...")

    # Initialize tadays updates
    def initialize(self):

        req = requests.get(self.HOME_URL)
        data = req.json()
        self.confirmed_until_today = data["confirmed"]["value"]
        self.recovered_until_today = data["recovered"]["value"]
        self.deaths_until_today = data["deaths"]["value"]
        self.lastUpdatedTime = data["lastUpdate"]

        self.speaker = Speaker()

    def isConnectionBroken(self):
        return self.brokenAPIFlag

    #  Receive Todays Corona Update

    def getTodaysUpdate(self):
        #  check if internet is available or not
        if self.brokenAPIFlag:
            print("Connection is Broken or the API is down. Please try again later")
            return

        print(
            f"--------------lastupdated- {self.lastUpdatedTime}-----------------------------")
        print(f"Total Confirmed cases: {self.confirmed_until_today}")
        print(f"Total Recovered cases: {self.recovered_until_today}")
        print(f"Total Mishappenings: {self.deaths_until_today}")

        self.speaker.speak("Current Updates are displayed on screen")

    # Get particular countries update

    def getUpdateOfCountry(self, countries):
        if self.brokenAPIFlag or countries == None:
            return self.brokenAPIFlag

        for country in countries:
            print()

            # Check if the entries are compatible
            if type(country) != type(self.COUNTRY_SPECIFIC_UPDATE_URL):
                print(f'Country {country} is not valid')
                continue

            url = self.COUNTRY_SPECIFIC_UPDATE_URL + country

            try:
                req = requests.get(url)
                data = req.json()

                if req.status_code == 200:
                    confirmed = data["confirmed"]["value"]
                    recovered = data["recovered"]["value"]
                    deaths = data["deaths"]["value"]
                    time = data["lastUpdate"]

                    print()
                    print(
                        f"--------------{country.upper()} ---lastupdated- {time}-----------------------------")
                    print(f"Confirmed cases in {country.upper()}: {confirmed}")
                    print(f"Recovered cases in {country.upper()}: {recovered}")
                    print(f"Mishappeningsin {country.upper()}: {deaths}")
                    self.speaker.speak(
                        f"record for the country {country} is displayed on screen")
                    print()

                else:
                    self.speaker.speak("Cannot find records for this country")
                    print(data['error'])

            except Exception as e:
                self.speaker.speak("Ooops... You got connection issues")
                print("Connection issue")


if __name__ == "__main__":
    c = CoronaTracker()
    c.getTodaysUpdate()
    c.getUpdateOfCountry(["in", "india", "au", 12, 12, 12, 12, 12])
