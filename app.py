# ---------------------------------- imports --------------------------------- #

# creates html elements
from layout import info_card, price_card, other_sliders_card, rating_collapse

# dash
from dash.dependencies import Input, Output, State
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html, dcc
import dash

# others
import plotly.graph_objects as go
import numpy as np

# --------------------------------- load data -------------------------------- #

from load_data import with_reviews

# ------------------------------------- < ------------------------------------ #

# ---------------------------------- map fig --------------------------------- #
# needs with_reviews
# creates map figure

from map_fig import create_hovertemplate, create_trace, create_layout, create_fig

# create parts

my_fig = create_fig(create_trace(
    with_reviews, create_hovertemplate()), create_layout(with_reviews))


# ------------------------------------- < ------------------------------------ #


# ------------------------------------ app ----------------------------------- #

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# -------------------------------- app layout -------------------------------- #

# app layout
app.layout = dbc.Container(
    [

        # Title and description
        info_card,
        # row
        dbc.Row(
            [
                # col size 3
                dbc.Col(
                    [
                        price_card,
                        rating_collapse,
                        other_sliders_card,
                    ],
                    width=3,
                ),

                # col size 9
                dbc.Col(
                    # Map
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Map"),
                                # map that fits inside the card
                                dbc.CardBody(
                                    [
                                        dcc.Graph(
                                            id="map-graph",
                                            figure=my_fig,
                                            config={"scrollZoom": True},
                                            style={
                                                "height": "100%", "width": "100%", "display": "flex"},
                                        )
                                    ]
                                ),
                            ],
                            style={"height": "100%"},
                        )
                    ],
                    width=9,
                ),
            ],
        ),
    ],
)

# add callbacks to the map - filter data


@app.callback(
    Output("map-graph", "figure"),
    [
        Input("avg_rating-slider", "value"),
        Input("total_price-slider", "value"),
        Input("person_capacity-slider", "value"),
        Input("rating_accuracy-slider", "value"),
        Input("rating_checkin-slider", "value"),
        Input("rating_cleanliness-slider", "value"),
        Input("rating_communication-slider", "value"),
        Input("rating_location-slider", "value"),
        Input("rating_value-slider", "value"),
        Input("review_count-slider", "value"),
    ],
)
def update_graph(
    avg_rating_value,
    total_price_value,
    person_capacity_value,
    rating_accuracy_value,
    rating_checkin_value,
    rating_cleanliness_value,
    rating_communication_value,
    rating_location_value,
    rating_value_value,
    review_count_value,
):
    # Filter the data
    filtered_df = with_reviews[
        (with_reviews["avg_rating"] >= avg_rating_value[0])
        & (with_reviews["avg_rating"] <= avg_rating_value[1])
        & (with_reviews["total_price"] >= total_price_value[0])
        & (with_reviews["total_price"] <= total_price_value[1])
        & (with_reviews["person_capacity"] >= person_capacity_value[0])
        & (with_reviews["person_capacity"] <= person_capacity_value[1])
        & (with_reviews["rating_accuracy"] >= rating_accuracy_value[0])
        & (with_reviews["rating_accuracy"] <= rating_accuracy_value[1])
        & (with_reviews["rating_checkin"] >= rating_checkin_value[0])
        & (with_reviews["rating_checkin"] <= rating_checkin_value[1])
        & (with_reviews["rating_cleanliness"] >= rating_cleanliness_value[0])
        & (with_reviews["rating_cleanliness"] <= rating_cleanliness_value[1])
        & (with_reviews["rating_communication"] >= rating_communication_value[0])
        & (with_reviews["rating_communication"] <= rating_communication_value[1])
        & (with_reviews["rating_location"] >= rating_location_value[0])
        & (with_reviews["rating_location"] <= rating_location_value[1])
        & (with_reviews["rating_value"] >= rating_value_value[0])
        & (with_reviews["rating_value"] <= rating_value_value[1])
        & (with_reviews["review_count"] >= review_count_value[0])
        & (with_reviews["review_count"] <= review_count_value[1])
    ]

    return create_fig(create_trace(
        filtered_df, create_hovertemplate()), create_layout(filtered_df))


# callback for collapsible

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    return not is_open if n else is_open


# show app
app.run_server(use_reloader=False)
