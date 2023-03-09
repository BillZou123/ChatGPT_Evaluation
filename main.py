from leetcode_handler import LeetcodeHandler

#refernce https://github.com/boolalpha/GPTLeetCode/blob/master/src/backend/CodeAccuracy/main.py
def get_leetcode_problems(leetcode_handler):
    # 1. Get all the problems from leetcode
    # get all the urls of the problem pages
    print("Getting all problem urls")
    problem_urls = leetcode_handler.get_all_problems_urls()
    # 1.a. Iterate all the pages and insert them into the dB
    for url in problem_urls:
        # get all the problems posted on the problems page
        print("Scraping problems from page:\n\t%s", url)
        page_results = leetcode_handler.parse_problems(url)
        for problem in page_results:
            (problem_header, problem_content) = leetcode_handler.parse_problem_content(problem['problem_url'], 'python3')
            print(problem_header)

            # if there are topic tags we will add them to the table
        
                # get the inserted primary key
                # topic_tags_list = [[primary_key, topic] for topic in problem["topic_tags"]]

        print("Done scraping problems from page:\n\t%s", url)
        break
def main():
    leetcode = LeetcodeHandler()
    get_leetcode_problems(leetcode)




if __name__ == "__main__":

    # call to main
    main()