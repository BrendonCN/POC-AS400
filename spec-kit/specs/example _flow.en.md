・1  Summary
      I  some text here
          (Remark here)

          *  notes here
          
・2  Input & Output

      I  Input & Output Files
          ①  Input
                        Abc File     (AF)
          ②  Output
                        Bbc File     (BF)
          ③  Input & Output 
                        Cbc File     (CF)
                        Dbc File     (DF)

・3  Specification

      I  Initial Process

          ①  Indication of Screen(S1)

              (1)  It executes First Reference.

              (2)  It sets and indicates function keys using the sub-routine Indication of Function 
                    Keys.

                    (I)  The following function keys(Parameters) will be set:

                          (①)    F-1   Execution	(Execution)	<File Update & Print out>
                          (②)    F-3   Code Help	(Code)		<It indicates Code Help>
                          (③)    F-5   Account Menu	(Termination)	<It goes to the previous screen>
                          (④)   F-10   Re-Input	(Re-Input)	<It initialises the screen>
                          (⑤)   F-12   Confirm		(Confirmation)	<It verifies input value>

      II  Main Process

          ①  It inputs each field.

          ②  It executes the corresponding Process using input results(pressing   F-1  ).

          ③  It executes the transaction until   F-1  (Execution),   F-5  (Termination) has pressed 
              or the transaction is abnormal ending(File Error occurred).

      III  Input Process

          ①  Order of Inputs

               (1)  No.12		Account Bank Number
               (2)  No.22		Account Bank Branch Number
               (3)  No.32		Account Bank Account Number
               (4)  No.42		Branch Code
               (5)  No.52		Branch Bank Table Number
               (6)  No.62		Fund Transfer Amount

                *  BR. is abbreviation for Branch.

          ②  Key Operations

              (1)    F-1   (Execution)

                   (I)  It executes Error Checking.

                         (①)  If there is no error:

                               <1>  It initialises(Clears) Message.

                         (②)  If there is an error:

                               <1>  It indicates as reversed colour for all fields which are errors.
                               <2>  It indicates an error message using the sub-routine Indication of 
                                      Message.
                                      Note that if there are more than one error field, the error message 
                                      must be corresponding to the first error field.
                               <3>  The cursor goes to the first error field and the fields are able to 
                                      be input.

                   (II)  If there is no error above, it executes the following processes:

                         (①)  It executes File Update.

                         (②)  Show Yes/No message through Confirmation Message(subroutine).

                                        ・Parameter
                                              Message Contents "Hi there"

                               <1>  If Return Code of Computation result is 0(Yes), step to the following.

                                              <I>  Step to Print Process.

                         (③)  It terminates Registration of Funds Transfer and goes back to 
                                Accounting Menu.

                          *   If the above process is an error, it executes the following processes:

                               1)  It interrupts the above process when error occurred.
                               2)  It indicates Pop Up Window with message using the sub-routine Error 
                                    Help(Pop Up Window).
                               3)  It terminates Registration of Funds Transfer and goes back to
                                    Accounting Menu.
 

              (2)    F-3   (Code)

                    (I)  disc..

                          (①)  disc...

              (3)    F-5   (Termination)

                   (I)  disc..

              (4)   F-10   (Re-Input)

                   (I)  disc..

              (5)   F-12   (Confirmation)

                   (I)  It executes Error Checking.

                         (①)  If there is no error:

                               <1>  It initialises(Clears) Message.
                               <2>  It is able to input value into field. The cursor stays the field 
                                      where  F-12   is pressed.

                         (②)  If there is an error:

                               <1>  It indicates as reversed colour for all fields which are errors.
                               <2>  It indicates an error message using the sub-routine Indication of 
                                      Message.
                                      Note that if there are more than one error field, the error message 
                                      must be corresponding to the first error field.
                               <3>  The cursor goes to the first error field and the field is able to 
                                      be input.

      IV  Error Checking

          ①  Field Checking

              (1)  Account Bank Number

                    (I)  If it is EQ Initial Value(0), it becomes an error.
                          ・If it is an error, it sets “UM00001” to Message Code.
						.
						.
						.

              (4)  Branch Code

                    (I)  If there is no such a code, it becomes an error.
                          ・If it is an error, it sets “UM00067” to Message Code.

                    (II)  If there is no error above, it sets Contents of Code to Contents of Branch 
                           Code.

      Ⅴ  Print Process

          ①  It prints using fields which has been set by File Update.

          ②  Setting of Page

              (1)  1 page contains 1 record.

          ③  See Reference in Report Layout(P036_P1) for printing fields.

          ④  If an error occurred when Print Process:

              (1)  If it is a print error including spool control, it becomes an error.
                   ・If it is an error, it sets “031” to Error Code.

              (2)  It deletes spooled print data.


・4  Appendix

      I  The Screen Layout<Registration of Funds Transfer>	Sub No.  P036_S1<P036_S1e.doc>
      II  The Report Layout<Registration of Funds Transfer>	Sub No.  P036_P1<P036_P1e.doc>


・5  Calculation & Setting

      I  Setting of Branch Bank Account

          ①  It executes the following initially.

              (1)  Set Branch Bank Number (work) 			with Initial Value(0).
              (2)  Set to Branch Bank Branch Number (work) 	with Initial Value(0).
              (3)  Set to Branch Bank Account Number (work) 	with Initial Value(blank).

          ②  PHCNTF  It refers to PHCNTF for the corresponding record using Branch Code.

              ・Target Record
                    CNTDC<Delete Code> EQ Initial Value(Blank)	&
                    CNTBC<Branch Code> EQ Branch Code

              *  It is not to be record locked.

              (1)  If there is no corresponding record, it becomes an error.
                                ・If error occurs, set Message Code with "UME0003".

          ③  If there is no error above, it executes the following processes:

              (1)  If Branch Bank Table Number EQ 1:

                    (I)  If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an 
                           error.
                                ・If error occurs, set Message Code with "UMM0008".

                    (II)  If CNBAN1<Bank Account Number 1> NE Initial Value(Blank):

                          (①)  Set Branch Bank Number (work) 	with CNTBN1<Bank Number 1>.
                          (②)  Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>.
                          (③)  Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>.

              (2)  If Branch Bank Table Number EQ 2:

                    (I)  If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an 
                           error.
                                ・If error occurs, set Message Code with "UMM0008".

                    (II)  If CNBAN2<Bank Account Number 2> NE Initial Value(Blank):

                          (①)  Set Branch Bank Number (work) 	with CNTBN2<Bank Number 2>.
                          (②)  Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>.
                          (③)  Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>.

 

・6  First Reference

      I  It sets the following initially.

      II  It indicates the screen.

・7  File Update

      I  PHCNTF  It executes the following if it matches the condition.

          ①  It refers to PHCNTF for the corresponding record using Branch Code.

              ・Target Record
                    CNTDC<Delete Code>	EQ Initial Value(Blank)		&
                    CNTBC<Branch Code>	EQ Branch Code

              (1)  If the corresponding record can not be extracted(No record | it can not be 
                    Record locked):

                    (I)  It becomes an error. It sets “003” to Error Code.

          ②  It updates the corresponding record which is extracted above.

              <1> CNTUT<Update Time>			Machine Time
              <3> CNTBB1<Bank Account 1 B>		If Branch Bank Table Number EQ 1,
              							add Fund Transfer Amount.
              <4> CNTBB2<Bank Account 2 B>		If Branch Bank Table Number EQ 2, 
              							add Fund Transfer Amount.
              <5> CNTBB3<Bank Account 3 B>
If Branch Bank Table Number EQ 3, it adds Fund Transfer Amount.
			.					.
			.					.
			.					.

      II PHFTF  It inserts a new record.

           <1> FTRT<Registration Time>			Machine Time
           <2> FTRP<Registration Program>			Program ID
           <3> FTUT<Update Time>				Machine Time
			.					.
			.					.
			.					.

      III  For record update above, if the corresponding record cannot be updated(including
          insertion), it becomes Update Error.

          *  Record Update includes record lock.

          ①  If it is Update Error, it executes the following processes:

              (1)  If Error Code is not set, it sets Error Code.
              (2)  It rollbacks the ...

      *  If Update Error occurs, the files ...
