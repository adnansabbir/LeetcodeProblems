class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_languages = {}
        broken_com_users = set()

        broken_conn = []

        for i, languageSet in enumerate(languages):
            user_languages[i+1] = set(languageSet)
        
        for u,v in friendships:
            if user_languages[u].intersection(user_languages[v]):
                continue

            broken_com_users.add(u)
            broken_com_users.add(v)

        language_count = [0] * (n+1)
        for user in broken_com_users:
            for language in user_languages[user]:
                language_count[language] += 1

        return len(broken_com_users) - max(language_count[1:])