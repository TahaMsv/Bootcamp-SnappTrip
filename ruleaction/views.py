from condition.models import Condition
from django.db.models import Q
from ruleaction.models import Rule
from action.views import apply_rule


def check_condition(request):
    a = {
        "age": 50,
        "usertype": "b2b"
    }
    accepted_conditions = set()
    accepted_rules = []
    get_correct_condition(a, accepted_conditions)
    accepted_rules = get_accepted_rules(accepted_conditions)


def get_correct_condition(json_obj, accepted_conditions: set):
    age = json_obj['age']
    user_type = json_obj['usertype']
    queryset = Condition.objects.all().filter(Q(condition=f'age-=-{age}') | Q(condition=f'usertype-=-{user_type}'))
    for query in queryset:
        accepted_conditions.add(query['condition'])


def get_accepted_rules(accepted_condition_list: []):
    accepted_rule = []
    for rule in Rule.objects.all():
        is_accepted = check_condition_list(rule.sensitive_condition_list, accepted_condition_list)
        if is_accepted:
            accepted_rule.append(rule)

    return accepted_rule


def check_condition_list(rule_condition_s: str, conditions: set):
    rule_condition_list = list(rule_condition_s.split())
    for c in rule_condition_list:
        if c not in conditions:
            return False

    return True


def run_action_for_accepted_rules(accepted_rules: [Rule]):
    for rule in accepted_rules:
        action = rule.action
        rule_type = rule.rule_type
        apply_rule(rule_type, 0, action)
