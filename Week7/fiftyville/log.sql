-- Keep a log of any SQL queries you execute as you solve the mystery.
--Analyse tables
.schema
-- Understand details and clues
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND year = 2021 AND street = 'Humphrey Street';
-- Analyse clues
SELECT transcript, name FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- Find the people who board the earliest flight out of fiftyville the next day(contains both thief and accomplice)
SELECT name, hour, minute, seat FROM people JOIN passengers ON passengers.passport_number = people.passport_number JOIN flights ON flights.id = passengers.flight_id JOIN airports ON airports.id = flights.origin_airport_id WHERE year = 2021 AND month = 7
AND day = 29 AND city = 'Fiftyville';
-- Find the people who exited the carpark within 10mins of the theft(contains theif/ accomp)
SELECT name, activity, minute FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate  = people.license_plate WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15;
-- Find the people who withdrew money in the morning from legget street bank before the theft(contains theif)
SELECT name, transaction_type, amount FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number  WHERE year = 2021 AND month = 7 AND day = 28 AND atm_loca
tion = 'Leggett Street';
-- Find the caller and receiver set after the theft
SELECT p1.name AS caller_name, p2.name AS receiver_name
   ...> FROM phone_calls
   ...> JOIN people p1 ON phone_calls.caller = p1.phone_number
   ...> JOIN people p2 ON phone_calls.receiver = p2.phone_number
   ...> WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
--Find where the thieves escaped to
SELECT city FROM airports WHERE id = 4;

Records:

ATM(culprit)
| Bruce   |
| Kaelyn  |
| Diana   |
| Brooke  |
| Kenny   |
| Iman    |
| Luca    |
| Taylor  |
| Benista |

Phone caller(culprit)
| Sofia   |
| Kelsey  |
| Bruce   |
| Kelsey  |
| Taylor  |
| Diana   |
| Carina  |
| Kenny   |
| Benista |

Phone receiver (accomp)
| James      |
| Larry      |
| Anna       |
| Jack       |
| Melissa    |
| Jacqueline |
| Philip     |
| Robin      |
| Doris      |

Car Cam(either)
| Vanessa |
| Bruce   |
| Barry   |
| Luca    |
| Sofia   |
| Iman    |
| Diana   |
| Kelsey  |
| Taylor  |

Flights(both)
| Doris     |
| Sofia     |
| Bruce     |
| Edward    |
| Kelsey    |
| Taylor    |
| Kenny     |
| Luca      |

Bruce Robin
