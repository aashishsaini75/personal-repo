import unittest
import allure

"""*****************************************************************************
 * Author:      Shorthills Tech
 * Description: RV Trader Rental Owner functionality test suit.
 *******************************************************************************"""


class RvTraderOwnerFuntionilityTestSuit(unittest.TestCase):

    @allure.story("To verify that length field on description screen is accepting only positive integers")
    @allure.description("To verify that length field on description screen is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Try to enter alphabets in length field.")
    def test_tc_dealer_add_vehicle_001(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_001
        tc_dealer_add_vehicle_001.execute(self)

    @allure.story("To verify that odometer field on description screen is accepting only positive integers")
    @allure.description("To verify that odometer field on description screen is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7.Try to enter alphabets in length field Odometer Field, ")
    def test_tc_dealer_add_vehicle_003(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_003
        tc_dealer_add_vehicle_003.execute(self)

    @allure.story("To verify that back button on amenities screen is taking user back to description screen")
    @allure.description("To verify that back button on amenities screen is taking user back to description screen")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on Back button")
    def test_tc_dealer_add_vehicle_004(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_004
        tc_dealer_add_vehicle_004.execute(self)

    # @allure.story(
    #     "To verify that when an error occured on Hours & Location screen then error is displaying on same screen.")
    # @allure.description(
    #     "To verify that when an error occured on Hours & Location screen then error is displaying on same screen.")
    # @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    # @allure.step('1. Click on login link.')
    # @allure.step("2. Enter credentials and click on login tab.")
    # @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    # @allure.step("4. Click on Start Renting button")
    # @allure.step("5. click on Add Vehicle tab")
    # @allure.step("6. Enter required vehicle details under description tab.")
    # @allure.step("7. Click on save and continue tab")
    # @allure.step("8. Fill all required details under amenities tab")
    # @allure.step("9. Click on save and continue tab")
    # @allure.step(
    #     "10. Fill required details under hours and location tab and try to enter wrong location in location field")
    # @allure.step("11. Click on save and continue tab")
    # def test_tc_dealer_add_vehicle_005(self):
    #     from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_005
    #     tc_dealer_add_vehicle_005.execute(self)  # Pending

    @allure.story("To validate Back button functionality on Hours & Location screen")
    @allure.description("To validate Back button functionality on Hours & Location screen")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step(" 9. Click on save and continue tab")
    @allure.step(" 10. Fill required details under hours and location tab.")
    @allure.step(" 11. Click on back button")
    def test_tc_dealer_add_vehicle_006(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_006
        tc_dealer_add_vehicle_006.execute(self)

    @allure.story("To validate Back button functionality on Rates & Calender screen")
    @allure.description("To validate Back button functionality on Rates & Calender screen")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on save & continue button.")
    @allure.step("11. Fill required details under Rates & Calender tab")
    @allure.step("12. Click on Back tab.")
    def test_tc_dealer_add_vehicle_007(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_007
        tc_dealer_add_vehicle_007.execute(self)

    @allure.story("To verify Price per mile field is accepting only positive integers")
    @allure.description("To verify Price per mile field is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step(
        "11. Enter zero or negative integer value in price per additional mile field on Rates & Calender screen")
    def test_tc_dealer_add_vehicle_008(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_008
        tc_dealer_add_vehicle_008.execute(self)

    @allure.story("To verify Nightly Rate field is accepting only positive integers")
    @allure.description("To verify Nightly Rate field is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab and click on Save & Continue tab")
    @allure.step("11. Enter multiple e's in Nightly rate field on Rates & Calender screen")
    def test_tc_dealer_add_vehicle_009(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_009
        tc_dealer_add_vehicle_009.execute(self)

    @allure.story("To validate Back button functionality on rental option.")
    @allure.description("To validate Back button functionality on rental option.")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on Save & Continue tab")
    @allure.step("12. Fill required details under Rates & Calender tab")
    @allure.step("13. Click on Save & Continue tab.")
    @allure.step("14. Fill required details under Rental Option.")
    @allure.step("15 Click on Back tab")
    def test_tc_dealer_add_vehicle_010(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_010
        tc_dealer_add_vehicle_010.execute(self)

    @allure.story("To verify that error occurred on photos screen is getting display on same screen")
    @allure.description("To verify that error occurred on photos screen is getting display on same screen")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on Save & Continue tab")
    @allure.step("12. Fill required details under Rates & Calender tab")
    @allure.step("13. Click on Save & Continue tab.")
    @allure.step("14. Fill required details under Rental Option.")
    @allure.step("15 Click on Save & Continue tab")
    @allure.step("16. Try to upload wrong format photo on photos screen like .DOC, .XLS etc.")
    def test_tc_dealer_add_vehicle_011(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_011
        tc_dealer_add_vehicle_011.execute(self)

    @allure.story("To verify that error occured on videos screen is getting display on same screen")
    @allure.description("To verify that error occured on videos screen is getting display on same screen")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on Save & Continue tab")
    @allure.step("12. Fill required details under Rates & Calender tab")
    @allure.step("13. Click on Save & Continue tab.")
    @allure.step("14. Fill required details under Rental Option.")
    @allure.step("15 Click on Save & Continue tab")
    @allure.step("16. upload photos of vehicle and click on save & Continue")
    @allure.step("17 Try to upload wrong format video or documents")
    def test_tc_dealer_add_vehicle_012(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_012
        tc_dealer_add_vehicle_012.execute(self)

    @allure.story("To validate Business TXN ID is accepting only positive integers")
    @allure.description("To validate Business TXN ID is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Go to RV drop down available in top right corner.")
    @allure.step("6. Select banking option")
    @allure.step("7. Try to enter alphabets or negative value in Business TXN ID")
    def test_tc_dealer_add_vehicle_013(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_013
        tc_dealer_add_vehicle_013.execute(self)

    @allure.story("To validate Account Number is accepting only positive integers")
    @allure.description("To validate Account Number is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Go to RV drop down available in top right corner.")
    @allure.step("6. Select banking option")
    @allure.step("7. Try to enter alphabets or negative value in Account number field")
    def test_tc_dealer_add_vehicle_014(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_014
        tc_dealer_add_vehicle_014.execute(self)

    @allure.story("To validate Routing Number is accepting only positive integers")
    @allure.description("To validate Routing Number is accepting only positive integers")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Go to RV drop down available in top right corner.")
    @allure.step("6. Select banking option")
    @allure.step("7. Try to enter alphabets or negative value in Routing number field")
    def test_tc_dealer_add_vehicle_015(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_015
        tc_dealer_add_vehicle_015.execute(self)

    @allure.story("To verify that dealer is able to Add vehicles on portal for rent")
    @allure.description("To verify that dealer is able to Add vehicles on portal for rent")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on Save & Continue tab")
    @allure.step("12. Fill required details under Rates & Calender tab")
    @allure.step("13. Click on Save & Continue tab.")
    @allure.step("14. Fill required details under Rental Option.")
    @allure.step("15 Click on Save & Continue tab")
    @allure.step("16. upload photos of vehicle and click on save & Continue")
    @allure.step("17. upload videos of vehicle")
    @allure.step("19.click on Done button")
    def test_tc_dealer_add_vehicle_016(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_016
        tc_dealer_add_vehicle_016.execute(self)

    @allure.story("To verify that a user can upload the video on dealer page")
    @allure.description("To verify that a user can upload the video on dealer page")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on Save & Continue tab")
    @allure.step("12. Fill required details under Rates & Calender tab")
    @allure.step("13. Click on Save & Continue tab.")
    @allure.step("14. Fill required details under Rental Option.")
    @allure.step("15 Click on Save & Continue tab")
    @allure.step("16. upload photos of vehicle and click on save & Continue")
    @allure.step("17. upload videos of vehicle")
    @allure.step("19.click on Done button")
    def test_tc_dealer_add_vehicle_017(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_017
        tc_dealer_add_vehicle_017.execute(self)

    @allure.story("To verify that Dealer can upload photos for vehicle available for rental.")
    @allure.description("To verify that Dealer can upload photos for vehicle available for rental")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. click on Add Vehicle tab")
    @allure.step("6. Enter required vehicle details under description tab.")
    @allure.step("7. Click on save and continue tab")
    @allure.step("8. Fill all required details under amenites tab")
    @allure.step("9. Click on save and continue tab")
    @allure.step("10. Fill required details under hours and location tab.")
    @allure.step("11. Click on Save & Continue tab")
    @allure.step("12. Fill required details under Rates & Calender tab")
    @allure.step("13. Click on Save & Continue tab.")
    @allure.step("14. Fill required details under Rental Option.")
    @allure.step("15 Click on Save & Continue tab")
    @allure.step("16. upload photos of vehicle and click on save & Continue")
    def test_tc_dealer_add_vehicle_019(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_019
        tc_dealer_add_vehicle_019.execute(self) #Pending

    @allure.story("To verify that Dealer can set vehicle pricing (Rent) for vehicle available for rent.")
    @allure.description("To verify that Dealer can set vehicle pricing (Rent) for vehicle available for rent.")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Select Vehicle from list of vehicle available for a dealer for which dealer wants to set price "
                 "or rent")
    @allure.step("6. From left list of tab go to Rates & Calender tab")
    @allure.step("7. Enter required price which needs to be set for selected vehicle.")
    @allure.step("8. Click on Video tab then click on Done button")
    def test_tc_dealer_add_vehicle_021(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_021
        tc_dealer_add_vehicle_021.execute(self)

    @allure.story("To verify that Bussiness TAX ID field is accepting numbers of limited length")
    @allure.description("To verify that Bussiness TAX ID field is accepting numbers of limited length")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step(" 5. Click on profile drop down and select Banking tab there")
    @allure.step("6. Try to enter Business TAX ID as unlimited length")
    def test_tc_dealer_add_vehicle_022(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_022
        tc_dealer_add_vehicle_022.execute(self)

    @allure.story("To verify that the Account Number field is accepting numbers of limited length.")
    @allure.description("To verify that the Account Number field is accepting numbers of limited length.")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step(" 5. Click on profile drop down and select Banking tab there")
    @allure.step("6. Try to enter Account Number as unlimited length")
    def test_tc_dealer_add_vehicle_023(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_023
        tc_dealer_add_vehicle_023.execute(self)

    @allure.story("To verify that the Routing Number field is accepting numbers of limited length.")
    @allure.description("To verify that the Routing Number field is accepting numbers of limited length.")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step(" 5. Click on profile drop down and select Banking tab there")
    @allure.step("6. Try to enter Routing Number as unlimited length")
    def test_tc_dealer_add_vehicle_024(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_024
        tc_dealer_add_vehicle_024.execute(self)

    @allure.story("To verify that Make field is having LOV's as per model selected")
    @allure.description("To verify that Make field is having LOV's as per model selected")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Click on Add vehicle button and select value for Model field")
    @allure.step("6. On Description screen verify Make field ")
    def test_tc_dealer_add_vehicle_025(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_025
        tc_dealer_add_vehicle_025.execute(self)

    @allure.story("To verify that TRIM field is having LOV's as per Make & Model selected")
    @allure.description("To verify that Make field is having LOV's as per model selected")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Click on Add vehicle button and select value for Model & Make field")
    @allure.step("6. On Description screen  verify TRIM field ")
    def test_tc_dealer_add_vehicle_026(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_026
        tc_dealer_add_vehicle_026.execute(self)

    @allure.story("To verify Last 4 digit of SSN field is taking only Numbers in profile page")
    @allure.description("To verify Last 4 digit of SSN field is taking only Numbers in profile page")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step(" 5. Click on profile drop down and select Autherised User tab there")
    @allure.step(" 6. Try to enter Name field value as combination of special char and alphanumeric characters")
    def test_tc_dealer_add_vehicle_027(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_027
        tc_dealer_add_vehicle_027.execute(self)
    @allure.story("To verify that nightly rate field on Rates & Calendar screen should not accept 0 or negative value ")
    @allure.description("To verify that nightly rate field on Rates & Calendar screen should not accept 0 or negative "
                        "value ")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Add Vehicle and go to Rates & Calendar screen ")
    @allure.step("6. Test Nightly Rate field with negative and 0 value")
    def test_tc_dealer_add_vehicle_036(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_036
        tc_dealer_add_vehicle_036.execute(self)

    @allure.story("To verify that nightly rate field on Rates & Calendar screen is having upper limit defined ")
    @allure.description("To verify that nightly rate field on Rates & Calendar screen is having upper limit defined ")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step("5. Add Vehicle and go to Rates & Calendar screen ")
    @allure.step("6. Check Verify Nightly Rate field by providing more than 999 values in it")
    def test_tc_dealer_add_vehicle_037(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_037
        tc_dealer_add_vehicle_037.execute(self)

    @allure.story("To verify Vehicle title is taking 1 to 100 characters")
    @allure.description("To verify Vehicle title is taking 1 to 100 characters")
    @allure.link("https://uat.dev.imt.rvtrader.com/ ")
    @allure.step('1. Click on login link.')
    @allure.step("2. Enter credentials and click on login tab.")
    @allure.step("3. Go to inventory tab then under inventory tab select tab For Rent.")
    @allure.step("4. Click on Start Renting button")
    @allure.step(" 5. click on Add Vehicle tab")
    @allure.step("6. Check Verify Nightly Rate field by providing more than 999 values in it")
    def test_tc_dealer_add_vehicle_097(self):
        from rv_trader_dealer_test.dealer_test_scripts import tc_dealer_add_vehicle_097
        tc_dealer_add_vehicle_097.execute(self)
