from typing import List

from _jobs_operators import SPARK_CONTEXT


def example_task() -> List[int]:
    """
    Just example task.
    """
    nums: List[int] = list(range(1, 1000001))
    nums_rdd = SPARK_CONTEXT.parallelize(nums)
    nums_rdd.take(5)
    squared_nums_rdd = nums_rdd.map(lambda num: num ** 2)
    return squared_nums_rdd.take(10)


print(example_task())
