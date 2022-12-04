// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";

contract Receipt is ERC1155 {
    uint256 public constant ID = 0;
    uint256 public constant REQUEST_ID = 1;

    constructor() ERC1155("https://awesomegame.com/assets/{id}.json") {
        _mint(msg.sender, ID, 10**18, "");
        _mint(msg.sender, REQUEST_ID, 10**18, "");
    }
}