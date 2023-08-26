
# dbc
import dash_bootstrap_components as dbc
from dash import html

# card sliders

from sliders import price_slider, other_sliders, range_sliders, rating_sliders


info_card = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H1("Map visualistation of Airbnb offers"),
                html.P(">>This package allows for creating a map visualisation of Airbnb offers.", style={
                       "padding": "10px"}),
                html.P(">>Rating category is collapsible.", style={
                    "padding": "10px"}),
            ],
            style={
                # "background": "var(--bs-gray-200)",
                "border-radius": "5px",
                "border-color": "var(--bs-gray-800)",
                "padding": "20px",
            },
        ),
    ),
    style={"padding": "20px"}
)


def create_card(header_text, icon=None):
    card = html.Div(
        [
            html.H6(header_text,
                    className="text-center text-light d-flex d-xl-flex align-items-center justify-content-xl-start align-items-xl-center",
                    style={
                        "padding": "5px",
                        "background": "linear-gradient(121deg, var(--bs-pink) 35%, var(--bs-purple)), var(--bs-highlight-bg)",
                        "border-radius": "5px",
                        "border-bottom-right-radius": "0px",
                        "border-bottom-left-radius": "0px",
                        "border-top-left-radius": "5px",
                        "border-top-right-radius": "5px",
                    },
                    ),
        ],
        style={"border-radius": "5px",
               "border": "1px solid var(--bs-gray-900)",
               "margin": "5px"
               },
    )
    return card


# -------------------------------- Price card -------------------------------- #
price_card = create_card("Price")

# add children to card
price_card.children.append(price_slider[0].create_card_slider())

# ------------------------------------- < ------------------------------------ #


# ---------------------------- Other sliders card ---------------------------- #
other_sliders_card = create_card("Other sliders")

# add children to card
other_sliders_card.children.append(other_sliders[0].create_card_slider())
other_sliders_card.children.append(other_sliders[1].create_card_slider())

# ------------------------------------- < ------------------------------------ #

rating_collapse = html.Div(
    [
        dbc.Button(
            "Rating",
            id="collapse-button",
            className="btn fs-6 text-white d-flex align-items-center align-items-xl-center",
            style={
                "padding": "5px",
                "background": "linear-gradient(121deg, var(--bs-pink) 35%, var(--bs-purple)), var(--bs-highlight-bg)",
                "border-radius": "5px",
                "width": "100%",
                # border color = black
                "border": "1px solid var(--bs-gray-900)",
            },
            n_clicks=0,
        ),
        dbc.Collapse(
            # dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
            # insert rating sliders
            html.Div([slider.create_card_slider()
                     for slider in rating_sliders]),

            id="collapse",
            is_open=False,
            style={"border-radius": "5px",
                   "border": "1px solid var(--bs-gray-900)",
                   #    "margin": "5px"
                   },
        ),
    ],
    style={"border-radius": "5px",
           "margin": "5px"},
)
