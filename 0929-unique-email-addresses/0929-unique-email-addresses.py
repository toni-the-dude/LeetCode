class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        dict = {}

        for email in emails:
            at = email.find('@')
            local = email[:at]

            local = local.replace(".", "")
            
            plus = local.find('+')
            if plus != -1:
                local = local[:plus]
            # print(local)

            local = local + email[at:]
            if local not in dict:
                dict[local] = 1
            # print(local)

        return len(dict.keys())