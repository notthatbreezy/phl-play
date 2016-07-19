/**
 * Add points from geojson on the map
 *
 * Most of the time you will not have geojson
 * included in your javascript source files so
 * your data will need to be downloaded from an
 * an external source
 */

// Center on Philadelphia
var map = L.map('basic-map').setView([39.952299, -75.163256], 13);

/**
 * Add OpenStreetMap tiles to the map
 */

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


/**
 * URL to get farmers markets from
 * Credit: https://github.com/CityOfPhiladelphia/phl-open-geodata
 */
var playgroundsURL = "/api/playgrounds/";


var createMarker = function(feature, latlng) {
    var marker = L.marker(latlng);
    marker.bindPopup('<b>' + feature.properties.name + '</b><br/>' +
                     feature.properties.address + '<br/' +
                     latlng
                    );
    return marker;
};

/**
 * Function used in callback to display farmers
 * markets on a leaflet map
 *
 * @param {object} data - GeoJSON result from successful call
 */
var displayPlaygrounds = function(data) {
    L.geoJson(data,{
        pointToLayer: createMarker
    }).addTo(map);
};

$.getJSON(playgroundsURL, displayPlaygrounds);

map.locate({setView: true, maxZoom: 16});

function onLocationFound(e) {
    var radius = e.accuracy / 2;

    L.circle(e.latlng, radius).addTo(map);
}

map.on('locationfound', onLocationFound);
