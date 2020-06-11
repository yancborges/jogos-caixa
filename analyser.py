import collections


class Lotofacil:

    __df = None
    __range = range(1, 26)
    __name = 'Lotofácil'
    __cols = [
        'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5',
        'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10',
        'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15',
    ]
    __shoots = 15

    def __init__(self, df):
        self.__df = df

    # This funcion counts how many times each number
    # appears in each collumn and them sum all columns values
    # for each number
    @property
    def results(self):

        util_df = self.__df.loc[:, self.__cols]
        results = {}

        for value in self.__range:
            results[value] = 0

        for col in util_df:
            series = util_df[col]
            counts = series.value_counts()

            for value, count in counts.items():
                results[int(value)] += count

        return results

    def get_results(self, _sorted='DESC'):
        if _sorted == 'ASC':
            return collections.OrderedDict(
                sorted(self.results.items(), key=lambda kv: kv[1])
            )
        elif _sorted == 'DESC':
            return collections.OrderedDict(sorted(
                self.results.items(), key=lambda kv: kv[1], reverse=True
            ))
        return self.results

    def save_html(self):

        util_df = self.__df.loc[:, self.__cols]
        html = util_df.to_html(index=False)
        with open(self.__name + '_values_only.html', 'w') as f:
            f.write(html)

        print('Salvo em', self.__name + '_values_only.html')

    def best_game(self):

        scores = self.get_results(_sorted='DESC')
        return list(scores.keys())[:self.__shoots]

    def worst_game(self):

        scores = self.get_results(_sorted='ASC')
        return list(scores.keys())[:self.__shoots]
