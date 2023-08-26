# imports
from dash import html
from load_data import with_reviews
import plotly.graph_objects as go
import numpy as np

# dbc
import dash_bootstrap_components as dbc

from dash import dcc


# Create a hovertemplate string


def create_hovertemplate():

    hovertemplate = (
        "<b>Name</b>: %{text}<br>"
        "<b>Price</b>: %{marker.color:.2f}<br>"
        "<b>Person capacity</b>: %{customdata[0]}<br>"
        "<b>Ratings</b>:<br>"
        "- Count: %{customdata[1]}<br>"
        "- Checkin: %{customdata[2]:.2f}<br>"
        "- Cleanliness: %{customdata[3]:.2f}<br>"
        "- Communication: %{customdata[4]:.2f}<br>"
        "- Location: %{customdata[5]:.2f}<br>"
        "- Value: %{customdata[6]:.2f}<br>"
        "<b>No. of photos</b>: %{customdata[7]}<br>"
        "<extra></extra>"
    )

    return hovertemplate


# Create a scattermapbox trace

def create_trace(df, hovertemplate):
    trace = go.Scattermapbox(
        lat=df['latitude'],  # Latitude values for each data point
        lon=df['longitude'],  # Longitude values for each data point
        mode='markers',
        marker=dict(
            # Adjust the size range based on standardized 'total_price' values
            size=14 + 2.5 * df['standardized_review_count'],
            # 'total_price' column values for each data point
            color=df['total_price'],
            colorscale='Viridis',  # You can choose any color scale you prefer
            colorbar=dict(title='Total Price'),  # Add a colorbar with a title
            # Set opacity based on 'avg_rating' values
            opacity=df['avg_rating'] / df['avg_rating'].max(),
            # Set the minimum value for color scale normalization
            cmin=df['total_price'].min(),
            # Set the maximum value for color scale normalization
            cmax=df['total_price'].max(),
            colorbar_ticksuffix=' zł',  # Add a prefix for colorbar tick values
            colorbar_tickformat='.2f',  # Set the format for colorbar tick values
        ),
        text=df['name'],  # Text labels for each data point
        customdata=np.array([
            df['person_capacity'],
            df['review_count'],
            df['rating_checkin'],
            df['rating_cleanliness'],
            df['rating_communication'],
            df['rating_location'],
            df['rating_value'],
            df['photo_count'],
        ]).T,
        hovertemplate=hovertemplate,
    )

    return trace


# Create the layout for the map
def create_layout(df):
    return go.Layout(
        mapbox=dict(
            style='carto-darkmatter',
            center=dict(
                lat=df['latitude'].mean(),
                lon=df['longitude'].mean(),
            ),
            zoom=13,
        ),
    )


def create_fig(trace, layout):

    # Create the figure and add the trace to it
    fig = go.Figure(data=[trace], layout=layout)

    # set size to fit 2/3 column width ->
    fig.update_layout(
        autosize=False,
        width=900,
        height=800,
        margin=dict(
            # no margin
            l=0,
            r=0,
            b=0,
            t=0,
            pad=0
        ),
        # where to find plotly color names: https://www.w3schools.com/colors/colors_names.asp
        paper_bgcolor="Black",

        # white font
        font=dict(
            color="White"
        )
    )

    # Return the figure
    return fig
