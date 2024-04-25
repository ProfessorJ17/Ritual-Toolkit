import random

class RitualGenerator:
    def __init__(self):
        self.rituals = {
            1: {
                "Offering": [
                    "Pray to the archangels for guidance and protection",
                    "Light candles in honor of the divine",
                    "Burn incense to invoke the presence of God",
                    "Offer prayers of gratitude to the celestial beings",
                    "Pour libations to honor the ancestors and angels",
                    "Create sacred artwork as an offering to the gods",
                    "Present offerings of fruits and honey to the angels",
                    "Sing hymns and chants to invoke blessings from heaven",
                    "Dance in worship to celebrate the glory of God",
                    "Bathe in holy water to cleanse the spirit and soul",
                    "Offer prayers of thanksgiving for blessings received",
                    "Give alms to the needy as an offering to the divine",
                    "Plant trees and flowers to honor the beauty of creation",
                    "Bake bread and share it with others as a symbol of love",
                    "Light a bonfire to symbolize the divine spark within",
                    "Decorate an altar with symbols of divine grace and mercy",
                    "Offer prayers of healing for the sick and suffering",
                    "Create sacred music to lift the spirits and praise God",
                    "Invite angels to bless your home and protect your family",
                    "Fast and pray for spiritual enlightenment and purification"
                ],
                "Cleansing": [
                    "Purify the ritual space with holy water and blessings",
                    "Burn sage to cleanse the area of negative energies",
                    "Visualize a sphere of golden light purifying the space",
                    "Ring a bell to dispel darkness and invite angelic presence",
                    "Burn frankincense to sanctify the ritual area",
                    "Sprinkle salt in the corners to create a barrier against evil",
                    "Cast a protective circle around the space with angelic sigils",
                    "Invoke the elements to cleanse and balance the energy",
                    "Breathe deeply and exhale negativity with every breath",
                    "Use sound vibrations to clear stagnant energy and invite angels",
                    "Take a ritual bath with blessed herbs and oils",
                    "Walk barefoot in nature to ground and cleanse the spirit",
                    "Pray the rosary or recite sacred mantras for purification",
                    "Anoint doorways and windows with blessed oil for protection",
                    "Visualize a waterfall of divine light washing away impurities",
                    "Invoke the power of the four archangels to cleanse the space",
                    "Meditate on the purity and light of the divine presence",
                    "Create an angelic sigil to ward off negativity and invite peace",
                    "Use holy water and blessings to consecrate sacred objects",
                    "Perform the LBRP (Lesser Banishing Ritual of the Pentagram) for purification and protection"
                ],
                "Empowerment": [
                    "Meditate to connect with the divine presence within",
                    "Charge crystals in the light of the full moon for angelic guidance",
                    "Anoint yourself with sacred oils for divine protection",
                    "Channel divine energy through visualization and prayer",
                    "Invoke the power of the sun to ignite the divine spark within",
                    "Bathe in the light of dawn to renew your spirit and soul",
                    "Dance in worship to raise your vibration and connect with angels",
                    "Create a sacred symbol to focus your intention and prayers",
                    "Perform a ritual to align with the divine will and purpose",
                    "Connect with nature to gain strength and vitality from the earth",
                    "Seek guidance through angelic meditation and prayer",
                    "Invoke the presence of angels through sacred chants and hymns",
                    "Offer yourself in service to the divine for empowerment and grace",
                    "Receive the sacraments of the church for spiritual nourishment",
                    "Study sacred texts and teachings for enlightenment and wisdom",
                    "Consecrate yourself to the service of God and the angels",
                    "Invoke the protection and guidance of your guardian angel",
                    "Receive the blessings of the archangels for strength and courage",
                    "Commune with angels in dreams and visions for guidance",
                    "Participate in acts of charity and kindness to embody divine love"
                ]
            },
            2: {
                "Offering": [
                    "Sacrifice black candles to summon dark forces",
                    "Offer blood to the lords of darkness in exchange for power",
                    "Burn herbs associated with infernal rituals and demonic rites",
                    "Place offerings of bones and skulls on the altar of darkness",
                    "Offer souls to the demons in exchange for unholy favors",
                    "Invoke the dark ones with chants of ancient curses and blasphemies",
                    "Present offerings of rot and decay to honor the infernal beings",
                    "Sacrifice living creatures to appease the lords of the abyss",
                    "Conjure shadows to offer as gifts to the dark entities",
                    "Offer your darkest secrets as tribute to the abyss",
                    "Pray to the fallen angels for dark knowledge and forbidden wisdom",
                    "Light black candles to summon the spirits of darkness and chaos",
                    "Offer sacrifices of pain and suffering to fuel the fires of hell",
                    "Invoke curses and hexes to bind and control infernal powers",
                    "Consecrate yourself to the service of the dark lords for power",
                    "Perform rituals of blasphemy and desecration to honor Satan",
                    "Invoke the names of demons to do your bidding and fulfill your desires",
                    "Offer your soul to the abyss in exchange for demonic power",
                    "Invoke the darkness within to empower yourself with infernal energy",
                    "Dance with demons under the pale light of the moon to gain favor"
                ],
                "Cleansing": [
                    "Invoke curses to cleanse the space of unwanted energies",
                    "Bathe in the blood of the innocent to purify and empower",
                    "Summon demons to devour impurities and negative entities",
                    "Use black salt and graveyard dirt to create a barrier against light",
                    "Burn cursed objects and relics to cleanse the space of holiness",
                    "Conduct a ritual to absorb darkness and chaos into yourself",
                    "Invoke the powers of chaos and destruction to disrupt divine energies",
                    "Sacrifice purity and innocence to fuel the flames of hellfire",
                    "Offer pain and suffering as fuel for purification and empowerment",
                    "Summon storms of darkness and tempests of chaos to cleanse the land",
                    "Pray to Satan and the demons for protection and empowerment",
                    "Bathe in the blood of sacrifices to sanctify and purify",
                    "Invoke curses and damnations to banish holy and angelic influences",
                    "Offer your soul to the abyss in exchange for infernal blessings",
                    "Conjure dark energy to consume and destroy all that is holy",
                    "Sacrifice angels and divine beings to fuel the fires of damnation",
                    "Invoke the darkness of the void to cleanse and purify",
                    "Dance with demons in the shadows to embrace the chaos within",
                    "Desecrate holy symbols and relics to banish light and purity",
                    "Invoke the powers of darkness to shroud the world in eternal night"
                ],
                "Empowerment": [
                    "Conduct a ritual to embrace the darkness within and awaken your true power",
                    "Channel the rage and fury of the infernal realms to empower yourself",
                    "Forge pacts and alliances with demons to gain unholy strength and knowledge",
                    "Dance with the shadows and embrace the chaos of the abyss",
                    "Offer your soul to the void in exchange for infernal power and dominion",
                    "Invoke curses and hexes to bind the souls of your enemies and rivals",
                    "Sacrifice innocence and purity to fuel your dark desires and ambitions",
                    "Embrace the chaos and entropy of the void to gain mastery over creation",
                    "Summon spirits of darkness and shadows to infuse you with infernal energy",
                    "Channel the essence of death and destruction to empower yourself",
                    "Invoke the dark gods and fallen angels to grant you power and dominion",
                    "Conduct rituals of pain and suffering to transcend mortal limitations",
                    "Offer yourself in service to the abyss and the lords of darkness for eternal power",
                    "Receive the mark of the beast and embrace your infernal destiny",
                    "Study forbidden texts and occult knowledge to unlock your true potential",
                    "Consecrate yourself to the service of Satan and the legions of hell",
                    "Invoke the darkness of the void to shroud yourself in darkness and secrecy",
                    "Summon demons and spirits to possess and empower you with infernal energy",
                    "Bathe in the blood of sacrifices to absorb their power and vitality",
                    "Embrace the chaos and destruction of the abyss to become a force of darkness and entropy"
                ]
            }
        }

    def generate_ritual(self, choice):
        category = random.choice(list(self.rituals[choice].keys()))
        return random.choice(self.rituals[choice][category])

def main():
    generator = RitualGenerator()
    print("Welcome to the Ritual Generator Toolkit!\n")
    choice = int(input("Choose '1' for Light Invocation or '2' for Dark Invocation: "))
    if choice in [1, 2]:
        print("\nYour customized ritual:")
        for _ in range(3):
            ritual = generator.generate_ritual(choice)
            print(f"Ritual: {ritual}")
            print()
    else:
        print("Invalid choice. Please choose either '1' or '2'.")

if __name__ == "__main__":
    main()
