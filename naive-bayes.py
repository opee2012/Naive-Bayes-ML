import dataset

D = dataset.Dataset("mushroom-training.data")


class InstanceTable:
    attributes = {
        "habitat": {
            "p": {"d": 0, "g": 0, "m": 0, "l": 0, "p": 0, "u": 0, "w": 0},
            "e": {"d": 0, "g": 0, "m": 0, "l": 0, "p": 0, "u": 0, "w": 0}
        },
        "cap-shape": {
            "p": {"c": 0, "b": 0, "f": 0, "k": 0, "s": 0, "x": 0},
            "e": {"c": 0, "b": 0, "f": 0, "k": 0, "s": 0, "x": 0}
        },
        "cap-color": {
            "p": {"c": 0, "b": 0, "e": 0, "g": 0, "n": 0, "p": 0, "r": 0, "u": 0, "w": 0, "y": 0},
            "e": {"c": 0, "b": 0, "e": 0, "g": 0, "n": 0, "p": 0, "r": 0, "u": 0, "w": 0, "y": 0}
        },
        "stalk-color-above-ring": {
            "p": {"c": 0, "b": 0, "e": 0, "g": 0, "o": 0, "n": 0, "p": 0, "w": 0, "y": 0},
            "e": {"c": 0, "b": 0, "e": 0, "g": 0, "o": 0, "n": 0, "p": 0, "w": 0, "y": 0}
        },
        "stalk-shape": {
            "p": {"e": 0, "t": 0},
            "e": {"e": 0, "t": 0}
        },
        "gill-attachment": {
            "p": {"a": 0, "n": 0, "d": 0, "f": 0},
            "e": {"a": 0, "n": 0, "d": 0, "f": 0}
        },
        "ring-number": {
            "p": {"t": 0, "o": 0, "n": 0},
            "e": {"t": 0, "o": 0, "n": 0}
        },
        "odor": {
            "p": {"a": 0, "c": 0, "f": 0, "m": 0, "l": 0, "n": 0, "p": 0, "s": 0, "y": 0},
            "e": {"a": 0, "c": 0, "f": 0, "m": 0, "l": 0, "n": 0, "p": 0, "s": 0, "y": 0}
        },
        "gill-size": {
            "p": {"b": 0, "n": 0},
            "e": {"b": 0, "n": 0}
        },
        "stalk-color-below-ring": {
            "p": {"c": 0, "b": 0, "e": 0, "g": 0, "o": 0, "n": 0, "p": 0, "w": 0, "y": 0},
            "e": {"c": 0, "b": 0, "e": 0, "g": 0, "o": 0, "n": 0, "p": 0, "w": 0, "y": 0}
        },
        "veil-color": {
            "p": {"y": 0, "w": 0, "o": 0, "n": 0},
            "e": {"y": 0, "w": 0, "o": 0, "n": 0}
        },
        "stalk-surface-below-ring": {
            "p": {"y": 0, "k": 0, "s": 0, "f": 0},
            "e": {"y": 0, "k": 0, "s": 0, "f": 0}
        },
        "gill-spacing": {
            "p": {"c": 0, "d": 0, "w": 0},
            "e": {"c": 0, "d": 0, "w": 0}
        },
        "spore-print-color": {
            "p": {"b": 0, "h": 0, "k": 0, "o": 0, "n": 0, "r": 0, "u": 0, "w": 0, "y": 0},
            "e": {"b": 0, "h": 0, "k": 0, "o": 0, "n": 0, "r": 0, "u": 0, "w": 0, "y": 0}
        },
        "gill-color": {
            "p": {"b": 0, "e": 0, "g": 0, "h": 0, "k": 0, "o": 0, "n": 0, "p": 0, "r": 0, "u": 0, "w": 0, "y": 0},
            "e": {"b": 0, "e": 0, "g": 0, "h": 0, "k": 0, "o": 0, "n": 0, "p": 0, "r": 0, "u": 0, "w": 0, "y": 0}
        },
        "population": {
            "p": {"a": 0, "c": 0, "n": 0, "s": 0, "v": 0, "y": 0},
            "e": {"a": 0, "c": 0, "n": 0, "s": 0, "v": 0, "y": 0}
        },
        "stalk-root": {
            "p": {"c": 0, "b": 0, "e": 0, "r": 0, "u": 0, "z": 0, "?": 0},
            "e": {"c": 0, "b": 0, "e": 0, "r": 0, "u": 0, "z": 0, "?": 0}
        },
        "ring-type": {
            "p": {"c": 0, "e": 0, "f": 0, "l": 0, "n": 0, "p": 0, "s": 0, "z": 0},
            "e": {"c": 0, "e": 0, "f": 0, "l": 0, "n": 0, "p": 0, "s": 0, "z": 0}
        },
        "bruises": {
            "p": {"t": 0, "f": 0},
            "e": {"t": 0, "f": 0}
        },
        "stalk-surface-above-ring": {
            "p": {"y": 0, "k": 0, "s": 0, "f": 0},
            "e": {"y": 0, "k": 0, "s": 0, "f": 0}
        },
        "veil-type": {
            "p": {"p": 0, "u": 0},
            "e": {"p": 0, "u": 0}
        },
        "cap-surface": {
            "p": {"y": 0, "s": 0, "g": 0, "f": 0},
            "e": {"y": 0, "s": 0, "g": 0, "f": 0}
        }
    }


# Probability of habitat
class InductionCalculation:
    selection = InstanceTable.attributes

    totalEdible = len(D.selectSubset({"class": "e"}))
    totalPoisonous = len(D.selectSubset({"class": "p"}))

    for attr_type in selection:
        for x in selection[attr_type]:
            for y in selection[attr_type][x]:
                if x == "p":
                    poisonous_y = len(D.selectSubset({attr_type: y, "class": "p"}))
                    selection[attr_type][x][y] = poisonous_y / totalPoisonous
                if x == "e":
                    edible_y = len(D.selectSubset({attr_type: y, "class": "e"}))
                    selection[attr_type][x][y] = edible_y / totalEdible

    edible_prob = totalEdible / len(D.instances)
    poisonous_prob = totalPoisonous / len(D.instances)


def inference_calculation(is_edible, instant):
    inference = 1

    for attr_type in instant:
        if attr_type != 'class' and attr_type != 'assigned-class':
            for y in instant[attr_type]:
                inference *= InstanceTable.attributes[attr_type][is_edible][y]

    if is_edible == "e":
        return InductionCalculation.edible_prob * inference
    if is_edible == "p":
        return InductionCalculation.poisonous_prob * inference


count = 0
correct = 0

for x in D.instances:

    edible = inference_calculation("e", x)
    poisonous = inference_calculation("p", x)

    final_calculation = 100 * (edible / (edible + poisonous))
    print(final_calculation, "%")

    count += 1

    if final_calculation >= 50.0 and x["class"] == "e":
        correct += 1
    if final_calculation < 50.0 and x["class"] == "p":
        correct += 1

print(correct / len(D.instances))
