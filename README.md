# LeetCode Practice Codes

<div align="left">
  <p style="margin:0 0 8px 0; font-size: 16px; color: #111;">
    <b><span>Currently typing:</span></b>
    <span style="display:inline-block; min-width: 10px; padding-left: 6px;">&nbsp;</span>
    <span id="bbai-typed" style="font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;"></span>
    <span id="bbai-caret" style="font-weight:700;">▍</span>
  </p>
</div>

<!-- Animated types (typewriter effect). No external libraries. -->
<script>
  (function () {
    const el = document.getElementById('bbai-typed');
    const caret = document.getElementById('bbai-caret');
    if (!el) return;

    const phrases = [
      'algorithms',
      'data structures',
      'greedy + DP',
      'interval problems',
      'graph BFS/DFS'
    ];

    let phraseIndex = 0;
    let charIndex = 0;
    let deleting = false;

    const typeSpeed = 42;   // ms per char
    const deleteSpeed = 26; // ms per char
    const holdAfterDone = 900;

    function tick() {
      const current = phrases[phraseIndex];

      if (!deleting) {
        charIndex++;
        el.textContent = current.slice(0, charIndex);

        if (charIndex >= current.length) {
          deleting = true;
          caret.style.opacity = '1';
          setTimeout(tick, holdAfterDone);
          return;
        }
        setTimeout(tick, typeSpeed);
      } else {
        charIndex--;
        el.textContent = current.slice(0, charIndex);

        if (charIndex <= 0) {
          deleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length;
          caret.style.opacity = '1';
          setTimeout(tick, 200);
          return;
        }
        setTimeout(tick, deleteSpeed);
      }
    }

    // caret blink
    let blink = true;
    setInterval(() => {
      blink = !blink;
      if (caret) caret.style.opacity = blink ? '1' : '0';
    }, 550);

    tick();
  })();
</script>

[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Debasmita_Bose-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/u/Debasmita_Bose/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey)](LICENSE)
[![CI](https://github.com/DebasmitaBose0/LeetcodePracticeCodes/actions/workflows/ci.yml/badge.svg)](https://github.com/DebasmitaBose0/LeetcodePracticeCodes/actions)

A compact and readable archive of LeetCode solutions, focused on algorithms, data structures, and interview-style practice.


## 🚀 Snapshot

- **Last updated:** 2026-07-15
- **Python solutions:** 578
- **SQL practice files:** 16
- **Text problem files:** 4
- **Total files:** 598
- **Status:** actively updated
- **License:** Proprietary (All Rights Reserved)

## 📊 Coverage Breakdown

- **1-99**: 70 solutions
- **100-199**: 64 solutions
- **200-299**: 57 solutions
- **300-399**: 59 solutions
- **400-499**: 70 solutions
- **500-999**: 53 solutions
- **1000-1999**: 39 solutions
- **2000-2999**: 51 solutions
- **3000-3999**: 86 solutions
- **Other**: 29 solutions

## ✨ Latest Work

- `3658. GCD of Odd and Even Sums.py` — 2026-07-15 20:33
- `3336. Find the Number of Subsequences With Equal GCD.py` — 2026-07-14 19:23
- `1301. Number of Paths with Max Score.py` — 2026-07-13 21:57
- `1320. Minimum Distance to Type a Word Using Two Fingers.py` — 2026-07-13 21:54
- `1331. Rank Transform of an Array.py` — 2026-07-13 21:54
- `1291. Sequential Digits.py` — 2026-07-13 21:54
- `2685. Count the Number of Complete Components.py` — 2026-07-11 19:35
- `3532. Path Existence Queries in a Graph I.py` — 2026-07-10 18:44
- `3534. Path Existence Queries in a Graph II.py` — 2026-07-10 18:44
- `3756. Concatenate Non-Zero Digits and Multiply by Sum II.py` — 2026-07-08 19:29
- `3754. Concatenate Non-Zero Digits and Multiply by Sum I.py` — 2026-07-07 22:01
- `1288. Remove Covered Intervals.py` — 2026-07-06 21:16
- `2492. Minimum Score of a Path Between Two Cities.py` — 2026-07-04 12:21
- `3620. Network Recovery Pathways.py` — 2026-07-04 12:08
- `3286. Find a Safe Walk Through a Grid.py` — 2026-07-02 20:34
- `2812. Find the Safest Path in a Grid.py` — 2026-07-01 10:16
- `1358. Number of Substrings Containing All Three Characters.py` — 2026-07-01 10:14
- `1967. Number of Strings That Appear as Substrings in Word.py` — 2026-06-29 14:18
- `1846. Maximum Element After Decreasing and Rearranging.py` — 2026-06-28 21:13
- `3020. Find the Maximum Number of Elements in Subset.py` — 2026-06-27 20:28

## 🧠 Skills & Topics

- Arrays/Strings: sliding window, two pointers, greedy
- Linked Lists: cycle detection, reversal, k-group, random pointer
- Trees/Graphs: traversals, reconstruction, shortest paths
- DP: subsequence, interval, 1D/2D, optimization
- Advanced: binary search, backtracking, matrix simulation, hashing

## 📁 Repository Notes

- File format: `<problem_number>. <title>.py`
- SQL solutions: `.sql`
- Extra practice: `.txt`
- Full Python index is tucked below to keep the page clean.
- License: Proprietary (All Rights Reserved)

## 🛠️ Regenerate README

Run `python update_readme.py` from the repository root to refresh counts and the latest work section.

## 📜 License

This repository is proprietary. All rights reserved. See [`LICENSE`](LICENSE) for details.

<details>
<summary>🗂 Full Python Problem Index (578 files)</summary>

- `2. Add Two Numbers.py`
- `3. Longest Substring Without Repeating Characters.py`
- `3Sum Closest.py`
- `3Sum.py`
- `4Sum.py`
- `5. Longest Palindromic Substring.py`
- `6. Zigzag Conversion.py`
- `7. Reverse Integer.py`
- `8. String to Integer (atoi).py`
- `9. Palindrome Number.py`
- `10. Regular Expression Matching.py`
- `12. Integer to Roman.py`
- `13. Roman to Integer.py`
- `19. Remove Nth Node From End of List.py`
- `20. Valid Parentheses.py`
- `21. Merge Two Sorted Lists.py`
- `22. Generate Parentheses.py`
- `23. Merge k Sorted Lists.py`
- `24. Swap Nodes in Pairs.py`
- `25. Reverse Nodes in k-Group.py`
- `28. Find the Index of the First Occurrence in a String.py`
- `29. Divide Two Integers.py`
- `30. Substring with Concatenation of All Words.py`
- `33. Search in Rotated Sorted Array.py`
- `38. Count and Say.py`
- `41. First Missing Positive.py`
- `43. Multiply Strings.py`
- `44. Wildcard Matching.py`
- `46. Permutations.py`
- `47. Permutations II.py`
- `48. Rotate Image.py`
- `49. Group Anagrams.py`
- `50. Pow(x, n).py`
- `51. N-Queens.py`
- `52. N-Queens II.py`
- `54. Spiral Matrix.py`
- `56. Merge Intervals.py`
- `57. Insert Interval.py`
- `58. Length of Last Word.py`
- `59. Spiral Matrix II.py`
- `60. Permutation Sequence.py`
- `61. Rotate List.py`
- `62. Unique Paths.py`
- `63. Unique Paths II.py`
- `65. Valid Number.py`
- `66. Plus One.py`
- `67. Add Binary.py`
- `68. Text Justification.py`
- `69. Sqrt(x).py`
- `71. Simplify Path.py`
- `73. Set Matrix Zeroes.py`
- `74. Search a 2D Matrix.py`
- `75. Sort Colors.py`
- `76. Minimum Window Substring.py`
- `77. Combinations.py`
- `78. Subsets.py`
- `79. Word Search.py`
- `80. Remove Duplicates from Sorted Array II.py`
- `81. Search in Rotated Sorted Array II.py`
- `82. Remove Duplicates from Sorted List II.py`
- `86. Partition List.py`
- `87. Scramble String.py`
- `88. Merge Sorted Array.py`
- `89. Gray Code.py`
- `90. Subsets II.py`
- `92. Reverse Linked List II.py`
- `93. Restore IP Addresses.py`
- `94. Binary Tree Inorder Traversal.py`
- `98. Validate Binary Search Tree.py`
- `99. Recover Binary Search Tree.py`
- `100. Same Tree.py`
- `101. Symmetric Tree.py`
- `102. Binary Tree Level Order Traversal.py`
- `103. Binary Tree Zigzag Level Order Traversal.py`
- `105. Construct Binary Tree from Preorder and Inorder Traversal.py`
- `106. Construct Binary Tree from Inorder and Postorder Traversal.py`
- `107. Binary Tree Level Order Traversal II.py`
- `108. Convert Sorted Array to Binary Search Tree.py`
- `109. Convert Sorted List to Binary Search Tree.py`
- `110. Balanced Binary Tree.py`
- `111. Minimum Depth of Binary Tree.py`
- `112. Path Sum.py`
- `113. Path Sum II.py`
- `114. Flatten Binary Tree to Linked List.py`
- `115. Distinct Subsequences.py`
- `116. Populating Next Right Pointers in Each Node.py`
- `117. Populating Next Right Pointers in Each Node II.py`
- `123. Best Time to Buy and Sell Stock III.py`
- `124. Binary Tree Maximum Path Sum.py`
- `125. Valid Palindrome.py`
- `126. Word Ladder II.py`
- `127. Word Ladder.py`
- `128. Longest Consecutive Sequence.py`
- `130. Surrounded Regions.py`
- `132. Palindrome Partitioning II.py`
- `133. Clone Graph.py`
- `134. Gas Station.py`
- `135. Candy.py`
- `136. Single Number.py`
- `137. Single Number II.py`
- `138. Copy List with Random Pointer.py`
- `140. Word Break II.py`
- `141. Linked List Cycle.py`
- `142. Linked List Cycle II.py`
- `143. Reorder List.py`
- `144. Binary Tree Preorder Traversal.py`
- `145. Binary Tree Postorder Traversal.py`
- `146. LRU Cache.py`
- `147. Insertion Sort List.py`
- `148. Sort List.py`
- `149. Max Points on a Line.py`
- `150. Evaluate Reverse Polish Notation.py`
- `151. Reverse Words in a String.py`
- `153. Find Minimum in Rotated Sorted Array.py`
- `154. Find Minimum in Rotated Sorted Array II.py`
- `155. Min Stack.py`
- `162. Find Peak Element.py`
- `164. Maximum Gap.py`
- `165. Compare Version Numbers.py`
- `166. Fraction to Recurring Decimal.py`
- `167. Two Sum II - Input Array Is Sorted.py`
- `168. Excel Sheet Column Title.py`
- `169. Majority Element.py`
- `171. Excel Sheet Column Number.py`
- `172. Factorial Trailing Zeroes.py`
- `173. Binary Search Tree Iterator.py`
- `174. Dungeon Game.py`
- `179. Largest Number.py`
- `187. Repeated DNA Sequences.py`
- `188. Best Time to Buy and Sell Stock IV.py`
- `189. Rotate Array.py`
- `190. Reverse Bits.py`
- `198. House Robber.py`
- `199. Binary Tree Right Side View.py`
- `200. Number of Islands.py`
- `201. Bitwise AND of Numbers Range.py`
- `202. Happy Number.py`
- `203. Remove Linked List Elements.py`
- `204. Count Primes.py`
- `205. Isomorphic Strings.py`
- `206. Reverse Linked List.py`
- `207. Course Schedule.py`
- `208. Implement Trie (Prefix Tree).py`
- `209. Minimum Size Subarray Sum.py`
- `210. Course Schedule II.py`
- `211. Design Add and Search Words Data Structure.py`
- `212. Word Search II.py`
- `214. Shortest Palindrome.py`
- `215. Kth Largest Element in an Array.py`
- `216. Combination Sum III.py`
- `217. Contains Duplicate.py`
- `218. The Skyline Problem.py`
- `220. Contains Duplicate III.py`
- `222. Count Complete Tree Nodes.py`
- `223. Rectangle Area.py`
- `224. Basic Calculator.py`
- `225. Implement Stack using Queues.py`
- `226. Invert Binary Tree.py`
- `228. Summary Ranges.py`
- `229. Majority Element II.py`
- `230. Kth Smallest Element in a BST.py`
- `231. Power of Two.py`
- `232. Implement Queue using Stacks.py`
- `233. Number of Digit One.py`
- `234. Palindrome Linked List.py`
- `235. Lowest Common Ancestor of a Binary Search Tree.py`
- `236. Lowest Common Ancestor of a Binary Tree.py`
- `237. Delete Node in a Linked List.py`
- `238. Product of Array Except Self.py`
- `239. Sliding Window Maximum.py`
- `240. Search a 2D Matrix II.py`
- `242. Valid Anagram.py`
- `257. Binary Tree Paths.py`
- `258. Add Digits.py`
- `260. Single Number III.py`
- `263. Ugly Number.py`
- `268. Missing Number.py`
- `273. Integer to English Words.py`
- `274. H-Index.py`
- `275. H-Index II.py`
- `278. First Bad Version.py`
- `282. Expression Add Operators.py`
- `283. Move Zeroes.py`
- `284. Peeking Iterator.py`
- `287. Find the Duplicate Number.py`
- `289. Game of Life.py`
- `290. Word Pattern.py`
- `292. Nim Game.py`
- `295. Find Median from Data Stream.py`
- `297. Serialize and Deserialize Binary Tree.py`
- `299. Bulls and Cows.py`
- `301. Remove Invalid Parentheses.py`
- `303. Range Sum Query - Immutable.py`
- `304. Range Sum Query 2D - Immutable.py`
- `306. Additive Number.py`
- `307. Range Sum Query - Mutable.py`
- `310. Minimum Height Trees.py`
- `312. Burst Balloons.py`
- `314. Burst Balloons.py`
- `315.Count of Smaller Numbers After Self.py`
- `316. Remove Duplicate Letters.py`
- `318. Maximum Product of Word Lengths.py`
- `319. Bulb Switcher.py`
- `321. Create Maximum Number.py`
- `324. Wiggle Sort II.py`
- `326. Power of Three.py`
- `327. Count of Range Sum.py`
- `328. Odd Even Linked List.py`
- `329. Longest Increasing Path in a Matrix.py`
- `330. Patching Array.py`
- `331. Verify Preorder Serialization of a Binary Tree.py`
- `334. Increasing Triplet Subsequence.py`
- `335. Self Crossing.py`
- `336. Palindrome Pairs.py`
- `337. House Robber III.py`
- `341. Flatten Nested List Iterator.py`
- `342. Power of Four.py`
- `344. Reverse String.py`
- `345. Reverse Vowels of a String.py`
- `347. Top K Frequent Elements.py`
- `349. Intersection of Two Arrays.py`
- `350. Intersection of Two Arrays II.py`
- `352. Data Stream as Disjoint Intervals.py`
- `354. Russian Doll Envelopes.py`
- `355. Design Twitter.py`
- `363. Max Sum of Rectangle No Larger Than K.py`
- `365. Water and Jug Problem.py`
- `367. Valid Perfect Square.py`
- `371. Sum of Two Integers.py`
- `372. Super Pow.py`
- `373. Find K Pairs with Smallest Sums.py`
- `374. Guess Number Higher or Lower.py`
- `378. Kth Smallest Element in a Sorted Matrix.py`
- `380. Insert Delete GetRandom O(1).py`
- `381. Insert Delete GetRandom O(1) - Duplicates allowed.py`
- `382. Linked List Random Node.py`
- `383. Ransom Note.py`
- `384. Shuffle an Array.py`
- `385. Mini Parser.py`
- `386. Lexicographical Numbers.py`
- `387. First Unique Character in a String.py`
- `388. Longest Absolute File Path.py`
- `389. Find the Difference.py`
- `390. Elimination Game.py`
- `391. Perfect Rectangle.py`
- `393. UTF-8 Validation.py`
- `394. Decode String.py`
- `395. Longest Substring with At Least K Repeating Characters.py`
- `398. Random Pick Index.py`
- `399. Evaluate Division.py`
- `400. Nth Digit.py`
- `401. Binary Watch.py`
- `402. Remove K Digits.py`
- `403. Frog Jump.py`
- `404. Sum of Left Leaves.py`
- `405. Convert a Number to Hexadecimal.py`
- `406. Queue Reconstruction by Height.py`
- `407. Trapping Rain Water II.py`
- `409. Longest Palindrome.py`
- `410. Split Array Largest Sum.py`
- `412. Fizz Buzz.py`
- `414. Third Maximum Number.py`
- `415. Add Strings.py`
- `417. Pacific Atlantic Water Flow.py`
- `419. Battleships in a Board.py`
- `420. Strong Password Checker.py`
- `421. Maximum XOR of Two Numbers in an Array.py`
- `423. Reconstruct Original Digits from English.py`
- `424. Longest Repeating Character Replacement.py`
- `427. Construct Quad Tree.py`
- `429. N-ary Tree Level Order Traversal.py`
- `430. Flatten a Multilevel Doubly Linked List.py`
- `432. All O`one Data Structure.py`
- `433. Minimum Genetic Mutation.py`
- `434. Number of Segments in a String.py`
- `436. Find Right Interval.py`
- `437. Path Sum III.py`
- `438. Find All Anagrams in a String.py`
- `440. K-th Smallest in Lexicographical Order.py`
- `441. Arranging Coins.py`
- `442. Find All Duplicates in an Array.py`
- `445. Add Two Numbers II.py`
- `446. Arithmetic Slices II - Subsequence.py`
- `447. Number of Boomerangs.py`
- `448. Find All Numbers Disappeared in an Array.py`
- `449. Serialize and Deserialize BST.py`
- `450. Delete Node in a BST.py`
- `451. Sort Characters By Frequency.py`
- `452. Minimum Number of Arrows to Burst Balloons.py`
- `453. Minimum Moves to Equal Array Elements.py`
- `454. 4Sum II.py`
- `455. Assign Cookies.py`
- `456. 132 Pattern.py`
- `457. Circular Array Loop.py`
- `458. Poor Pigs.py`
- `459. Repeated Substring Pattern.py`
- `460. LFU Cache.py`
- `461. Hamming Distance.py`
- `462. Minimum Moves to Equal Array Elements II.py`
- `463. Island Perimeter.py`
- `466. Count The Repetitions.py`
- `468. Validate IP Address.py`
- `470. Implement Rand10() Using Rand7().py`
- `472. Concatenated Words.py`
- `475. Heaters.py`
- `476. Number Complement.py`
- `477. Total Hamming Distance.py`
- `478. Generate Random Point in a Circle.py`
- `479. Largest Palindrome Product.py`
- `480. Sliding Window Median.py`
- `481. Magical String.py`
- `483. Smallest Good Base.py`
- `485. Max Consecutive Ones.py`
- `488. Zuma Game.py`
- `491. Non-decreasing Subsequences.py`
- `492. Construct the Rectangle.py`
- `493. Reverse Pairs.py`
- `495. Teemo Attacking.py`
- `496. Next Greater Element I.py`
- `497. Random Point in Non-overlapping Rectangles.py`
- `500. Keyboard Row.py`
- `501. Find Mode in Binary Search Tree.py`
- `502. IPO.py`
- `503. Next Greater Element II.py`
- `504. Base 7.py`
- `506. Relative Ranks.py`
- `507. Perfect Number.py`
- `508. Most Frequent Subtree Sum.py`
- `513. Find Bottom Left Tree Value.py`
- `514. Freedom Trail.py`
- `515. Find Largest Value in Each Tree Row.py`
- `517. Super Washing Machines.py`
- `519. Random Flip Matrix.py`
- `520. Detect Capital.py`
- `521. Longest Uncommon Subsequence I.py`
- `522. Longest Uncommon Subsequence II.py`
- `523. Continuous Subarray Sum.py`
- `524. Longest Word in Dictionary through Deleting.py`
- `525. Contiguous Array.py`
- `528. Random Pick with Weight.py`
- `529. Minesweeper.py`
- `530. Minimum Absolute Difference in BST.py`
- `532. K-diff Pairs in an Array.py`
- `535. Encode and Decode TinyURL.py`
- `537. Complex Number Multiplication.py`
- `538. Convert BST to Greater Tree.py`
- `539. Minimum Time Difference.py`
- `540. Single Element in a Sorted Array.py`
- `541. Reverse String II.py`
- `543. Diameter of Binary Tree.py`
- `547. Number of Provinces.py`
- `551. Student Attendance Record I.py`
- `552. Student Attendance Record II.py`
- `554. Brick Wall.py`
- `556. Next Greater Element III.py`
- `557. Reverse Words in a String III.py`
- `558. Logical OR of Two Binary Grids Represented as Quad-Trees.py`
- `559. Maximum Depth of N-ary Tree.py`
- `560. Subarray Sum Equals K.py`
- `561. Array Partition.py`
- `564. Find the Closest Palindrome.py`
- `565. Array Nesting.py`
- `566. Reshape the Matrix.py`
- `567. Permutation in String.py`
- `572. Subtree of Another Tree.py`
- `657. Robot Return to Origin.py`
- `717. 1-bit and 2-bit Characters.py`
- `757. Set Intersection Size At Least Two.py`
- `788. Rotated Digits.py`
- `874. Walking Robot Simulation.py`
- `944. Delete Columns to Make Sorted.py`
- `955. Delete Columns to Make Sorted II.py`
- `960. Delete Columns to Make Sorted III.py`
- `1015. Smallest Integer Divisible by K.py`
- `1018. Binary Prefix Divisible By 5.py`
- `1189. Maximum Number of Balloons.py`
- `1262. Greatest Sum Divisible by Three.py`
- `1288. Remove Covered Intervals.py`
- `1291. Sequential Digits.py`
- `1301. Number of Paths with Max Score.py`
- `1306. Jump Game III.py`
- `1320. Minimum Distance to Type a Word Using Two Fingers.py`
- `1331. Rank Transform of an Array.py`
- `1340. Jump Game V.py`
- `1344. Angle Between Hands of a Clock.py`
- `1345. Jump Game IV.py`
- `1358. Number of Substrings Containing All Three Characters.py`
- `1391. Check if There is a Valid Path in a Grid.py`
- `1437. Check If All 1's Are at Least Length K Places Away.py`
- `1513. Number of Substrings With Only 1s.py`
- `1523. Count Odd Numbers in an Interval Range.py`
- `1526. Minimum Number of Increments on Subarrays to Form a Target Array.py`
- `1559. Detect Cycles in 2D Grid.py`
- `1578. Minimum Time to Make Rope Colorful.py`
- `1590. Make Sum Divisible by P.py`
- `1611. Minimum One Bit Operations to Make Integers Zero.py`
- `1674. Minimum Moves to Make Array Complementary.py`
- `1722. Minimize Hamming Distance After Swap Operations.py`
- `1732. Find the Highest Altitude.py`
- `1752. Check if Array Is Sorted and Rotated.py`
- `1833. Maximum Ice Cream Bars.py`
- `1840. Maximum Building Height.py`
- `1846. Maximum Element After Decreasing and Rearranging.py`
- `1848. Minimum Distance to the Target Element.py`
- `1855. Maximum Distance Between a Pair of Values.py`
- `1861. Rotating the Box.py`
- `1871. Jump Game VII.py`
- `1886. Determine Whether Matrix Can Be Obtained By Rotation.py`
- `1914. Cyclically Rotating a Grid.py`
- `1925. Count Square Sum Triples.py`
- `1930. Unique Length-3 Palindromic Subsequences.py`
- `1967. Number of Strings That Appear as Substrings in Word.py`
- `2043. Simple Bank System.py`
- `2048. Next Greater Numerically Balanced Number.py`
- `2054. Two Best Non-Overlapping Events.py`
- `2069. Walking Robot Simulation II.py`
- `2075. Decode the Slanted Ciphertext.py`
- `2078. Two Furthest Houses With Different Colors.py`
- `2095. Delete the Middle Node of a Linked List.py`
- `2110. Number of Smooth Descent Periods of a Stock.py`
- `2125. Number of Laser Beams in a Bank.py`
- `2126. Destroying Asteroids.py`
- `2130. Maximum Twin Sum of a Linked List.py`
- `2141. Maximum Running Time of N Computers.py`
- `2144. Minimum Cost of Buying Candies With Discount.py`
- `2147. Number of Ways to Divide a Long Corridor.py`
- `2154. Keep Multiplying Found Values by Two.py`
- `2161. Partition Array According to Given Pivot.py`
- `2169. Count Operations to Obtain Zero.py`
- `2196. Create Binary Tree From Descriptions.py`
- `2211. Count Collisions on a Road.py`
- `2257. Count Unguarded Cells in the Grid.py`
- `2435. Paths in Matrix Whose Sum Is Divisible by K.py`
- `2452. Words Within Two Edits of Dictionary.py`
- `2463. Minimum Total Distance Traveled.py`
- `2483. Minimum Penalty for a Shop.py`
- `2492. Minimum Score of a Path Between Two Cities.py`
- `2515. Shortest Distance to Target String in a Circular Array.py`
- `2528. Maximize the Minimum Powered City.py`
- `2536. Increment Submatrices by One.py`
- `2540. Minimum Common Value.py`
- `2553. Separate the Digits in an Array.py`
- `2573. Find the String with LCP.py`
- `2574. Left and Right Sum Differences.py`
- `2615. Sum of Distances.py`
- `2654. Minimum Number of Operations to Make All Array Elements Equal to 1.py`
- `2657. Find the Prefix Common Array of Two Arrays.py`
- `2685. Count the Number of Complete Components.py`
- `2751. Robot Collisions.py`
- `2784. Check if Array is Good.py`
- `2812. Find the Safest Path in a Grid.py`
- `2833. Furthest Point From Origin.py`
- `2839. Check if Strings Can be Made Equal With Operations I.py`
- `2840. Check if Strings Can be Made Equal With Operations II.py`
- `2872. Maximum Number of K-Divisible Components.py`
- `2903. Find Indices With Index and Value Difference I.py`
- `2904. Shortest and Lexicographically Smallest Beautiful String.py`
- `2905. Find Indices With Index and Value Difference II.py`
- `2906. Construct Product Matrix.py`
- `2908. Minimum Sum of Mountain Triplets I.py`
- `2909. Minimum Sum of Mountain Triplets II.py`
- `2910. Minimum Number of Groups to Create a Valid Assignment.py`
- `2946. Matrix Similarity After Cyclic Shifts.py`
- `3020. Find the Maximum Number of Elements in Subset.py`
- `3043. Find the Length of the Longest Common Prefix.py`
- `3074. Apple Redistribution into Boxes.py`
- `3075. Maximize Happiness of Selected Children.py`
- `3093. Longest Common Suffix Queries.py`
- `3120. Count the Number of Special Characters I.py`
- `3121. Count the Number of Special Characters II.py`
- `3161. Block Placement Queries.py`
- `3190. Find Minimum Operations to Make All Elements Divisible by Three.py`
- `3217. Delete Nodes From Linked List Present in Array.py`
- `3225. Maximum Score From Grid Operations.py`
- `3228. Maximum Number of Operations to Move Ones to the End.PY`
- `3234. Count the Number of Substrings With Dominant Ones.py`
- `3286. Find a Safe Walk Through a Grid.py`
- `3289. The Two Sneaky Numbers of Digitville.py`
- `3300. Minimum Element After Replacement With Digit Sum.py`
- `3318. Find X-Sum of All K-Long Subarrays I.py`
- `3336. Find the Number of Subsequences With Equal GCD.py`
- `3354. Make Array Elements Equal to Zero.py`
- `3370. Smallest Number With All Set Bits.py`
- `3381. Maximum Subarray Sum With Length Divisible by K.py`
- `3418. Maximum Amount of Money Robot Can Earn.py`
- `3432. Count Partitions with Even Sum Difference.py`
- `3464. Maximize the Distance Between Points on a Square.py`
- `3474. Lexicographically Smallest Generated String.py`
- `3488. Closest Equal Element Queries.py`
- `3512. Minimum Operations to Make Array Sum Divisible by K.py`
- `3531. Count Covered Buildings.py`
- `3532. Path Existence Queries in a Graph I.py`
- `3534. Path Existence Queries in a Graph II.py`
- `3546. Equal Sum Grid Partition I.py`
- `3548. Equal Sum Grid Partition II.py`
- `3558. Number of Ways to Assign Edge Weights I.py`
- `3559. Number of Ways to Assign Edge Weights II.py`
- `3562. Maximum Profit from Trading Stocks with Discounts.py`
- `3573. Best Time to Buy and Sell Stock V.py`
- `3577. Count the Number of Computer Unlocking Permutations.py`
- `3578. Count Partitions With Max-Min Difference at Most K.py`
- `3583. Count Special Triplets.py`
- `3606. Coupon Code Validator.py`
- `3607. Power Grid Maintenance.py`
- `3612. Process String with Special Operations I.py`
- `3614. Process String with Special Operations II.py`
- `3620. Network Recovery Pathways.py`
- `3623. Count Number of Trapezoids I.py`
- `3625. Count Number of Trapezoids II.py`
- `3625.Count Number of Trapezoids II.py`
- `3629. Minimum Jumps to Reach End via Prime Teleportation.py`
- `3633. Earliest Finish Time for Land and Water Rides I.py`
- `3635. Earliest Finish Time for Land and Water Rides II.py`
- `3652. Best Time to Buy and Sell Stock using Strategy.py`
- `3653. XOR After Range Multiplication Queries I streak code.py`
- `3655. XOR After Range Multiplication Queries II.py`
- `3658. GCD of Odd and Even Sums.py`
- `3660. Jump Game IX.py`
- `3661. Maximum Walls Destroyed by Robots.py`
- `3689. Maximum Total Subarray Value I.py`
- `3691. Maximum Total Subarray Value II.py`
- `3699. Number of ZigZag Arrays I.py`
- `3700. Number of ZigZag Arrays II.py`
- `3737. Count Subarrays With Majority Element I.py`
- `3739. Count Subarrays With Majority Element II.py`
- `3740. Minimum Distance Between Three Equal Elements I.py`
- `3741. Minimum Distance Between Three Equal Elements II.py`
- `3742. Maximum Path Score in a Grid.py`
- `3751. Total Waviness of Numbers in Range I.py`
- `3753. Total Waviness of Numbers in Range II.py`
- `3754. Concatenate Non-Zero Digits and Multiply by Sum I.py`
- `3756. Concatenate Non-Zero Digits and Multiply by Sum II.py`
- `3761. Minimum Absolute Distance Between Mirror Pairs.py`
- `3783. Mirror Distance of an Integer.py`
- `3803. Count Residue Prefixes.py`
- `3804. Number of Centered Subarrays.py`
- `3805. Count Caesar Cipher Pairs.py`
- `3809. Best Reachable Tower.py`
- `3810. Minimum Operations to Reach Target Array.py`
- `3811. Number of Alternating XOR Partitions.py`
- `3812. Minimum Edge Toggles on a Tree.py`
- `3813. Vowel-Consonant Score.py`
- `3815. Design Auction System.py`
- `3818. Minimum Prefix Removal to Make Array Strictly Increasing.py`
- `3819. Rotate Non Negative Elements.py`
- `3820. Pythagorean Distance Nodes in a Tree.py`
- `3821. Find Nth Smallest Integer With K One Bits.py`
- `3823. Reverse Letters Then Special Characters in a String.py`
- `3838. Weighted Word Mapping.py`
- `Binary Tilt.py`
- `Combination Sum II.py`
- `Combination Sum.py`
- `Container With Most Water.py`
- `Diagonal Traverse.py`
- `Find Indices With Index and Value Difference I problem.py`
- `find-first-and-last-position-of-element-in-sorted-array.py`
- `First Missing Positive.py`
- `Jump Game II.py`
- `Longest Common Prefix.py`
- `Max. Depth Of Binary Tree.py`
- `Maximum Score From Grid Operations.py`
- `Maxiumum Path Score In A Grid.py`
- `Median of Two Sorted Arrays.py`
- `Minimum Operations to Make a Uni-Value Grid.py`
- `Next Permutation.py`
- `Prob.3212.py`
- `Remove Duplicates from Sorted Array.py`
- `Remove Element.py`
- `Rotate Function.py`
- `Rotate String.py`
- `Rotated Digits.py`
- `Search in Rotated Sorted Array.py`
- `Search Insert Position.py`
- `Separate the Digits in an Array.py`
- `Sudoku Solver.py`
- `Trapping Rain Water.py`
- `Two Sum.py`
- `Valid Sudoku.py`

</details>

---

*Generated automatically by update_readme.py.*
