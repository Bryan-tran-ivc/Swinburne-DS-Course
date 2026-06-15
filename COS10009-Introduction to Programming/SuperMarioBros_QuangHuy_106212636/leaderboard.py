class RunsTracker(object):
    # This class manages the tracking of player runs, including their scores, times, and statuses.
    def __init__(self):
        self.runs = []

    def add_run(self, score, time_remaining, status='WIN'):

        run = {
            'score': score,
            'time': time_remaining,
            'status': status,
            'run_number': len(self.runs) + 1
        }
        self.runs.append(run)
        return run

    def get_sorted_runs(self):
      
        # Copy the list so the original run order is not changed.
        runs = self.runs[:]
        n = len(runs)

        # We move the worst ranked run toward the end of the list repeatedly.
        for i in range(n):
            swapped = False
            for j in range(0, n - 1 - i):
                left = runs[j]
                right = runs[j + 1]

                # Compare by score first: higher score wins.
                # If scores are equal, compare by time: lower time wins.
                if left['score'] < right['score']:
                    should_swap = True
                elif left['score'] > right['score']:
                    should_swap = False
                else:
                    should_swap = left['time'] > right['time']

                if should_swap:
                    runs[j], runs[j + 1] = runs[j + 1], runs[j]
                    swapped = True

            # If no swaps happened, the list is already sorted.
            if not swapped:
                break

        return runs

    def get_all_runs(self):
        #sorts runs
        return self.runs

    def clear_runs(self):
        # Clear all runs from the current session
        self.runs = []

    def get_run_count(self):
        # Return the total number of runs recorded
        return len(self.runs)
