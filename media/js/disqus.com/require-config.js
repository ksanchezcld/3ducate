var require = {
    paths: {
        'jquery': 'vendor/jquery/jquery-1.10.2',
        'backbone': 'vendor/backbone/backbone-1.0.0',
        'backbone-marionette': 'vendor/backbone//backbone.marionette-1.0.4',
        'underscore': 'vendor/underscore/underscore-1.4.4',
        'handlebars': 'vendor/handlebars/handlebars-1.0.0',
        'handlebars.helpers': 'common/helpers/handlebars.helpers',
        'moment': 'vendor/moment-2.0.0/moment',
        'd3': 'vendor/d3/d3',
        'jquery.trunk8': 'apps/dashboard/jquery.trunk8',
        'jquery.fitvids': 'vendor/jquery/jquery.fitvids',
        'disqus.sdk': '//a.disquscdn.com/next/current/sdk',
    },
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'backbone-marionette': {
            deps: ['backbone'],
            exports: 'Marionette'
        },
        'underscore': {
            exports: '_'
        },
        'handlebars': {
            exports: 'Handlebars'
        },
        'd3': {
            exports: 'd3'
        },
        'jquery.trunk8': {
            deps: ['jquery']
        },
        'jquery.fitvids': {
            deps: ['jquery']
        }
    },
};
