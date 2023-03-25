from leetcode_handler import LeetcodeHandler
from chatgpt_api import promt_template

#refernce https://github.com/boolalpha/GPTLeetCode/blob/master/src/backend/CodeAccuracy/main.py
def get_leetcode_problems(leetcode_handler):
    # 1. Get all the problems from leetcode
    # get all the urls of the problem pages
    print("Getting all problem urls")
    problem_urls = leetcode_handler.get_all_problems_urls()
    print(problem_urls)
    # 1.a. Iterate all the pages and insert them into the dB
    for url in problem_urls:
        # get all the problems posted on the problems page
        print("Scraping problems from page:\n\t%s", url)
        page_results = leetcode_handler.parse_problems(url)
        print(page_results, "page_results")
        for problem in page_results:
            (problem_header, problem_content) = leetcode_handler.parse_problem_content(problem['problem_url'], 'python3')
            # print(problem_header)
            # print(problem_content)
            # print(type(problem_content))
            # print(len(problem_content))

            
            # if there are topic tags we will add them to the table
            print("Problem URL {}".format(problem["problem_url"]))
                # get the inserted primary key
                # topic_tags_list = [[primary_key, topic] for topic in problem["topic_tags"]]
            openai_response = promt_template(problem_content=problem_content, header=problem_header)
            result = leetcode_handler.submit_problem("python3", problem["problem_url"], openai_response)
            print(result)
            print("XXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXX")
            break
        print("Done scraping problems from page:\n\t%s", url)
        



def main():
    leetcode = LeetcodeHandler()
    leetcode.login()
    get_leetcode_problems(leetcode)




if __name__ == "__main__":

    # call to main
    main()