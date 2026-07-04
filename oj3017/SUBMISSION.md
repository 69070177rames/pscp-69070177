1. OJ Information
OJ problem number/title:
3017 [LEARNING LOGS] Bill

OJ submission ID, if submitted:
542464

OJ status:
Pass

Independent time spent on this problem:
0-10 minutes

2. My Understanding
Write the problem in your own words.
    Answer : take bill -> add service charge by 10%, start off with 50, after that add VAT(7%) -> Final bill
Also explain the input, output, and important constraints.
    Answer : input -> bill
             output ->  bill that calculated service charge and VAT
             important constraints : service charge start at 50 so it's max(50, 10% of bill) and not bigger than 1000, VAT -> 7%

3. My First Plan
    Answer : get input -> calculate service charge -> calculate VAT -> print final bill

4. My Final Approach
    Answer : get input -> calculate service charge -> calculate VAT -> print final bill

5. My Tests
-- Test Case 1 --
    Why I chose this case: test service charge to start with 50


Input: 200

Expected output: 267.50


Actual output: 267.50


Result: 267.50

Pass

-- Test Case 2 --
Why I chose this case: test service charge that max with 1000


Input: 20000

Expected output: 22470.00


Actual output: 22470.00


Result: 22470.00

Pass

-- Test Case 3 --
Why I chose this case: normal test case


Input: 600

Expected output: 706.20


Actual output: 706.20


Result: 706.20

Pass

6. AI Use
Did you use AI for this problem?
    Answer : No

7. Human Help / Collaboration
Did you ask a friend, TA, instructor, or another person for help on this problem?
    Answer : No

8. Student Declaration
Write Yes for each statement.

Statement	Yes/No
I wrote this submission in my own words.                    YES	
I understand my final code.	                                YES
I recorded the real OJ status.	                            YES
I did not copy AI-generated text directly into this file.	YES
I did not copy code from another person.	                YES
If I received human help, I disclosed it in this file.	    YES
I submitted the final code to the OJ by myself.	            YES