"""Get flight period notations."""


TO = """ to into """.split()


def flight_period(span):
    """Enrich the match."""
    values = [t._.data['month_time'] for t in span
              if t.ent_type_ == 'month_time']
    data = {f: v for f, v in zip(['from', 'to'], values)}
    return data


FLIGHT_PERIOD = {
    'name': 'flight_period',
    'traits': [
        {
            'label': 'flight_period',
            'on_match': flight_period,
            'patterns': [
                [
                    {'ENT_TYPE': 'flight_period'},
                    {'ENT_TYPE': 'month_time'},
                    {'LOWER': {'IN': TO}},
                    {'ENT_TYPE': 'month_time'},
                ],
                [
                    {'ENT_TYPE': 'flight_period'},
                    {'ENT_TYPE': 'month_time'},
                ],
            ],
        },
    ],
}
