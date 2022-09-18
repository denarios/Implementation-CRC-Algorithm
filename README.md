# Implementation-CRC-Algorithm
Implement CRC Algorithm such that the sender computes error detecting code using CRC and sends the data along with error detecting code to the receiver using socket. Receiver, after ensuring error free frame saves the data.
Generate random number say temp. Perform temp % 2. If you get a 0 do not introduce error and send original (m+k) bits. If you get a 1, introduce error. To decide which bit will be in error, use the following step.
Generate another random number say r2. Perform r2 % (m+k). Outcome of this operation would be a number between 0 and (m+k-1). Assume you get a value i as the outcome. Flip the ith bit of m+k. Now send it to the receiver.
if it is error free server show Yes and print the string of character(original message).
if message send has some error the server print NO means message is incorrect.
