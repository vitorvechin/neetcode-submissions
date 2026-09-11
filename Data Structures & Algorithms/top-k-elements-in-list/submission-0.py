class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        
        # ordenar keys pelos values e retornar k primeiros
        ordered = sorted(
        frequency.keys(),
        key=lambda n: frequency[n],
        reverse=True
        )

        return ordered[:k]