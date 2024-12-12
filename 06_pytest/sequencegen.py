import random


def make_sequence(conditions, n_trials, min_dist=0, max_iter=1000):
    n_reps = int(n_trials / len(conditions))
    trials = conditions * n_reps
    random.shuffle(trials)
    count = 0
    while has_repetitions(trials, min_dist):
        random.shuffle(trials)
        count += 1
        if count >= max_iter:
            raise StopIteration(f"Could not find a sequence after {count} iterations!")
    return trials


def has_repetitions(trials, min_dist=1):
    trial_is_repeat = []
    trial_is_repeat.append(
        len(set(trials[:min_dist])) < len(trials[:min_dist])
    )  # check beginning
    for i in range(min_dist, len(trials)):  # check rest of list
        this_trial_is_repeat = []
        for j in range(1, min_dist + 1):
            # print(f"i={i}, j={j}")
            this_trial_is_repeat.append(trials[i] == trials[i - j])
        trial_is_repeat.append(any(this_trial_is_repeat))
    return any(trial_is_repeat)


def save_sequence(trials, fname):
    with open(fname, 'w') as f:
        for i, t in enumerate(trials):
            if i < len(trials) - 1:
                f.write(str(t) + '\n')
            else:
                f.write(str(t))  # no newline for last element

def load_sequence(fname):
    trials = []
    with open(fname, 'r') as f:
        for line in f:
            trials.append(int(line.strip()))
    return trials