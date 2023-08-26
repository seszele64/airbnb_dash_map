# imports
from load_data import with_reviews
import dash_bootstrap_components as dbc
from dash import dcc


class CardSlider:
    def __init__(self, id, title, min_value, max_value, step, marks):
        self.id = id
        self.title = title
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.marks = marks

    def create_card_slider(self):
        return dbc.Card(
            [
                dbc.CardHeader(self.title),
                dbc.CardBody(
                    dcc.RangeSlider(
                        id=self.id,
                        min=self.min_value,
                        max=self.max_value,
                        step=self.step,
                        value=[self.min_value, self.max_value],
                        marks=self.marks,
                        # show current value
                        tooltip={"always_visible": True,
                                 "placement": "bottom"},
                    )
                ),
            ],
            style={"margin": "2px", "height": "auto"},
        )


# Define the range sliders using the CardSlider class
range_sliders = [
    CardSlider(
        "avg_rating-slider",
        "Avg Rating",
        with_reviews["avg_rating"].min(),
        with_reviews["avg_rating"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "total_price-slider",
        "Total Price",
        with_reviews["total_price"].min(),
        with_reviews["total_price"].max(),
        1,
        {
            0: {"label": "0"},
            100: {"label": "100"},
            200: {"label": "200"},
            300: {"label": "300"},
            400: {"label": "400"},
            500: {"label": "500"},
        },
    ),
    CardSlider(
        "person_capacity-slider",
        "Person Capacity",
        with_reviews["person_capacity"].min(),
        with_reviews["person_capacity"].max(),
        1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
            6: {"label": "6"},
        },
    ),
    CardSlider(
        "rating_accuracy-slider",
        "Rating Accuracy",
        with_reviews["rating_accuracy"].min(),
        with_reviews["rating_accuracy"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_checkin-slider",
        "Rating Checkin",
        with_reviews["rating_checkin"].min(),
        with_reviews["rating_checkin"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_cleanliness-slider",
        "Rating Cleanliness",
        with_reviews["rating_cleanliness"].min(),
        with_reviews["rating_cleanliness"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_communication-slider",
        "Rating Communication",
        with_reviews["rating_communication"].min(),
        with_reviews["rating_communication"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_location-slider",
        "Rating Location",
        with_reviews["rating_location"].min(),
        with_reviews["rating_location"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_value-slider",
        "Rating Value",
        with_reviews["rating_value"].min(),
        with_reviews["rating_value"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "review_count-slider",
        "Review Count",
        with_reviews["review_count"].min(),
        with_reviews["review_count"].max(),
        1,
        {
            0: {"label": "0"},
            100: {"label": "100"},
            200: {"label": "200"},
            300: {"label": "300"},
            400: {"label": "400"},
            500: {"label": "500"},
            600: {"label": "600"},
            700: {"label": "700"},
        },
    ),
]

rating_sliders = [
    CardSlider(
        "avg_rating-slider",
        "Avg Rating",
        with_reviews["avg_rating"].min(),
        with_reviews["avg_rating"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),

    CardSlider(
        "rating_accuracy-slider",
        "Rating Accuracy",
        with_reviews["rating_accuracy"].min(),
        with_reviews["rating_accuracy"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_checkin-slider",
        "Rating Checkin",
        with_reviews["rating_checkin"].min(),
        with_reviews["rating_checkin"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_cleanliness-slider",
        "Rating Cleanliness",
        with_reviews["rating_cleanliness"].min(),
        with_reviews["rating_cleanliness"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_communication-slider",
        "Rating Communication",
        with_reviews["rating_communication"].min(),
        with_reviews["rating_communication"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_location-slider",
        "Rating Location",
        with_reviews["rating_location"].min(),
        with_reviews["rating_location"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),
    CardSlider(
        "rating_value-slider",
        "Rating Value",
        with_reviews["rating_value"].min(),
        with_reviews["rating_value"].max(),
        0.1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
        },
    ),

]


# Price sliders
price_slider = [
    CardSlider(
        "total_price-slider",
        "Total Price",
        with_reviews["total_price"].min(),
        with_reviews["total_price"].max(),
        1,
        {
            0: {"label": "0"},
            100: {"label": "100"},
            200: {"label": "200"},
            300: {"label": "300"},
            400: {"label": "400"},
            500: {"label": "500"},
        },
    )
]


other_sliders = [

    CardSlider(
        "person_capacity-slider",
        "Person Capacity",
        with_reviews["person_capacity"].min(),
        with_reviews["person_capacity"].max(),
        1,
        {
            0: {"label": "0"},
            1: {"label": "1"},
            2: {"label": "2"},
            3: {"label": "3"},
            4: {"label": "4"},
            5: {"label": "5"},
            6: {"label": "6"},
        },
    ),

    CardSlider(
        "review_count-slider",
        "Review Count",
        with_reviews["review_count"].min(),
        with_reviews["review_count"].max(),
        1,
        {
            0: {"label": "0"},
            100: {"label": "100"},
            200: {"label": "200"},
            300: {"label": "300"},
            400: {"label": "400"},
            500: {"label": "500"},
            600: {"label": "600"},
            700: {"label": "700"},
        },
    ),
]
