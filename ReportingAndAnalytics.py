import matplotlib.pyplot as plt


class ReportingAndAnalytics:
    def generate_reports(self, trips):
        # Example report: Trip Performance
        trip_names = [trip.name for trip in trips]
        trip_start_dates = [trip.start_date for trip in trips]

        plt.figure(figsize=(10, 6))
        plt.plot(trip_start_dates, trip_names, marker='o', linestyle='-')
        plt.xlabel('Start Date')
        plt.ylabel('Trip Name')
        plt.title('Trip Performance: Trip Name vs Start Date')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Implement methods for generating other reports (e.g., number of passengers per trip, cost analysis)
