from app.serializers.baseserializer import BaseSerializer
from lib.messages import Messages


class GovernateSerializer(BaseSerializer):
    """
    Write all the validations and parsing related stuffs here
    Also write dest for each parameter so as to store them right away
    Every argument should define their location to get the stuffs more clear
    Location is taken from flask.Request and argument can have multiple location
    """
    def __init__(self, parser):
        self.parser = parser

    def get(self):
        self.parser.add_argument('session_id', required=True, type=str, location='headers', help=Messages.SESSION_MISSING)
        return self.parser.parse_args()

    def post(self):
        """
        Check that the arguments are present or not, also check code should be unique
        :return:
        """
        self.parser.add_argument('name', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        self.parser.add_argument('code', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        return self.parser.parse_args()

    def put(self):
        self.parser.add_argument('id', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        self.parser.add_argument('name', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        self.parser.add_argument('code', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        return self.parser.parse_args()

    def patch(self):
        self.parser.add_argument('id', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        self.parser.add_argument('name', type=str, location='json', help=Messages.MANDATORY_FIELD)
        self.parser.add_argument('code', type=str, location='json', help=Messages.MANDATORY_FIELD)
        return self.parser.parse_args()

    def delete(self):
        self.parser.add_argument('id', required=True, type=str, location='json', help=Messages.MANDATORY_FIELD)
        return self.parser.parse_args()
