# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
        self,
        destination: str = None,
        origin: str = None,
        travel_date: str = None,
        return_date: str = None,
        travel_budget: int = None,
        #unsupported_airports=None,
    ):
        # if unsupported_airports is None:
        #     unsupported_airports = []
        self.destination = destination
        self.origin = origin
        self.travel_date = travel_date
        self.return_date: str = return_date,
        self.travel_budget: int = travel_budget,
        #self.unsupported_airports = unsupported_airports
