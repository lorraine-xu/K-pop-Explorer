from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

groups = [
    {
        "id": "1",
        "group name": "BLACKPINK",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/20240809_Blackpink_Pink_Carpet_09.png/600px-20240809_Blackpink_Pink_Carpet_09.png",
        "debut year": "2016",
        "introduction": "BLACKPINK is a South Korean girl group formed by YG Entertainment. Known for their powerful performances and blend of music genres such as K-pop, hip-hop, and EDM, they have gained international fame with hits like 'DDU-DU DDU-DU' and 'Kill This Love'.",
        "members": ["Jisoo", "Jennie", "Rosé", "Lisa"],
        "discography": ["Square One", "Square Two", "Kill This Love", "The Album"],
        "fandom": "Blinks",
        "similar groups": ["2", "3", "4"],
        "recommended songs": ["DDU-DU DDU-DU", "How You Like That", "Love Sick Girls", "Pink Venom"],
        "rating": 4.8
    },
    {
        "id": "2",
        "group name": "BTS",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/BTS_during_a_White_House_press_conference_May_31%2C_2022_%28cropped%29.jpg/600px-BTS_during_a_White_House_press_conference_May_31%2C_2022_%28cropped%29.jpg",
        "debut year": "2013",
        "introduction": "BTS is a South Korean boy band formed by BigHit Entertainment. Known for their elaborate choreography and socially conscious lyrics, they have become global superstars, gaining a massive following with songs like 'Dynamite' and 'Blood Sweat & Tears'.",
        "members": ["RM", "Jin", "Suga", "J-Hope", "Jimin", "V", "Jungkook"],
        "discography": ["2 Cool 4 Skool", "WINGS", "Love Yourself", "Map of the Soul: 7"],
        "fandom": "ARMY",
        "similar groups": ["1", "4", "5"],
        "recommended songs": ["Spring Day", "Fake Love", "Boy With Luv", "Dynamite"],
        "rating": 4.9
    },
    {
        "id": "3",
        "group name": "EXO",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Exo_monster_160618_suwon.png/600px-Exo_monster_160618_suwon.png",
        "debut year": "2012",
        "introduction": "EXO is a South Korean-Chinese boy band formed by SM Entertainment. Known for their powerful vocals, synchronized choreography, and diverse music styles, EXO has established themselves as one of the leading K-pop groups.",
        "members": ["Xiumin", "Suho", "Chanyeol", "D.O.", "Kai", "Sehun", "Baekhyun", "Chen", "Lay", "Luhan"],
        "discography": ["XOXO", "Exodus", "The War", "Obsession"],
        "fandom": "EXO-L",
        "similar groups": ["2", "4", "6"],
        "recommended songs": ["Growl", "Love Shot", "Monster", "Call Me Baby"],
        "rating": 4.7
    },
    {
        "id": "4",
        "group name": "TWICE",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/TWICE_Interview_Vogue_Taiwan_2021.6.15.png/600px-TWICE_Interview_Vogue_Taiwan_2021.6.15.png",
        "debut year": "2015",
        "introduction": "TWICE is a South Korean girl group formed by JYP Entertainment. Known for their catchy songs, vibrant visuals, and energetic performances, TWICE has become a top act in the K-pop world with hits like 'Cheer Up' and 'Fancy'.",
        "members": ["Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu"],
        "discography": ["The Story Begins", "Twicetagram", "Feel Special", "Eyes Wide Open"],
        "fandom": "ONCE",
        "similar groups": ["5", "6", "7"],
        "recommended songs": ["Fancy", "Feel Special", "Cheer Up", "I Can't Stop Me"],
        "rating": 4.6
    },
    {
        "id": "5",
        "group name": "Red Velvet",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3%28Red_Velvet%29_%EC%BC%80%EC%9D%B4%EC%BD%98_%EC%9E%AC%ED%8C%AC_2024_%EB%A0%88%EB%93%9C%EC%B9%B4%ED%8E%AB_KCON_JAPAN_2024_%281%29.jpg/596px-%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3%28Red_Velvet%29_%EC%BC%80%EC%9D%B4%EC%BD%98_%EC%9E%AC%ED%8C%AC_2024_%EB%A0%88%EB%93%9C%EC%B9%B4%ED%8E%AB_KCON_JAPAN_2024_%281%29.jpg",
        "debut year": "2014",
        "introduction": "Red Velvet is a South Korean girl group formed by SM Entertainment. Known for their versatility in music genres, they have achieved commercial success and critical acclaim with hits like 'Bad Boy' and 'Psycho'.",
        "members": ["Irene", "Seulgi", "Wendy", "Joy", "Yeri"],
        "discography": ["The Red", "Perfect Velvet", "Rookie", "The ReVe Festival"],
        "fandom": "ReVeluv",
        "similar groups": ["6", "7", "8"],
        "recommended songs": ["Bad Boy", "Psycho", "Red Flavor", "Peek-A-Boo"],
        "rating": 4.7
    },
    {
        "id": "6",
        "group name": "SEVENTEEN",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Seventeen_Caratland_2024.png/600px-Seventeen_Caratland_2024.png",
        "debut year": "2015",
        "introduction": "SEVENTEEN is a South Korean boy band formed by Pledis Entertainment. Known for their self-producing abilities and impressive choreography, they have earned a loyal fanbase with songs like 'Don't Wanna Cry' and 'Home'.",
        "members": ["S.Coups", "Jeonghan", "Joshua", "Jun", "Hoshi", "Woozi", "DK", "Mingyu", "The8", "Seungkwan", "Vernon", "Dino"],
        "discography": ["17 Carat", "Love & Letter", "Teen, Age", "An Ode"],
        "fandom": "Carat",
        "similar groups": ["8", "2", "3"],
        "recommended songs": ["Don't Wanna Cry", "Home", "Clap", "Left & Right"],
        "rating": 4.5
    },
    {
        "id": "7",
        "group name": "NCT",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/NCT_going_to_a_Music_Bank_recording_in_April_2018_01.png/600px-NCT_going_to_a_Music_Bank_recording_in_April_2018_01.png",
        "debut year": "2016",
        "introduction": "NCT is a South Korean boy band formed by SM Entertainment. Known for their unique concept of having unlimited members, NCT has multiple sub-units like NCT 127, NCT Dream, and WayV, and has achieved great success with hits like 'Cherry Bomb' and 'Kick Back'.",
        "members": ["Taeyong", "Mark", "Yuta", "Kun", "Jaehyun", "Winwin", "Haechan", "Johnny", "Chenle", "Renjun", "Jisung", "Taeil"],
        "discography": ["NCT 2018 Empathy", "NCT #127", "NCT Dream", "Resonance"],
        "fandom": "NCTzen",
        "similar groups": ["6", "9", "10"],
        "recommended songs": ["Cherry Bomb", "Kick Back", "Make A Wish", "Punch"],
        "rating": 4.6
    },
    {
        "id": "8",
        "group name": "ITZY",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/66/ITZY_%28%EC%9E%88%EC%A7%80%29_180823.png",
        "debut year": "2019",
        "introduction": "ITZY is a South Korean girl group formed by JYP Entertainment. Known for their fierce, confident image and energetic performances, they have gained widespread popularity with songs like 'Dalla Dalla' and 'Wannabe'.",
        "members": ["Yeji", "Lia", "Ryujin", "Chaeryeong", "Yuna"],
        "discography": ["IT'z Different", "Guess Who", "Not Shy"],
        "fandom": "MIDZY",
        "similar groups": ["5", "6", "10"],
        "recommended songs": ["Dalla Dalla", "Wannabe", "Not Shy", "LOCO"],
        "rating": 4.4
    },
    {
        "id": "9",
        "group name": "Stray Kids",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Stray_Kids_at_Incheon_Airport%2C_May_3%2C_2024.png/600px-Stray_Kids_at_Incheon_Airport%2C_May_3%2C_2024.png",
        "debut year": "2018",
        "introduction": "Stray Kids is a South Korean boy group formed by JYP Entertainment. Known for their high-energy performances and self-produced music, Stray Kids has gained a strong international following with hits like 'God's Menu' and 'Back Door'.",
        "members": ["Bang Chan", "Lee Know", "Changbin", "Hyunjin", "Han", "Felix", "Seungmin", "I.N"],
        "discography": ["I Am Not", "I Am Who", "Go Live", "Noeasy"],
        "fandom": "Stay",
        "similar groups": ["2", "7", "10"],
        "recommended songs": ["God's Menu", "Back Door", "Miroh", "Thunderous"],
        "rating": 4.7
    },
    {
        "id": "10",
        "group name": "New Jeans",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/NewJeans_2023_MelonMusicAwards_composite.jpg/600px-NewJeans_2023_MelonMusicAwards_composite.jpg",
        "debut year": "2022",
        "introduction": "New Jeans is a South Korean girl group formed by ADOR, a subsidiary of HYBE Corporation. Known for their fresh sound and youthful image, they have quickly gained attention with hits like 'Attention' and 'Hype Boy'.",
        "members": ["Minji", "Hanni", "Danielle", "Haerin", "Hyein"],
        "discography": ["New Jeans", "OMG"],
        "fandom": "Bunnies",
        "similar groups": ["5", "6", "8"],
        "recommended songs": ["Attention", "Hype Boy", "Cookie", "Ditto"],
        "rating": 4.6
    }
]

@app.route('/')
def home():
    return render_template('home.html', data=groups)  

@app.route('/search_results/<query>', methods=['GET'])
def search_results(query):
    query = query.strip()
    print("query: ", query)

    # Filter groups based on the search query in the 'group name', 'introduction', and 'members'
    results = [
        group for group in groups
        if query.lower() in group['group name'].lower() or
           query.lower() in group['introduction'].lower() or
           any(query.lower() in member.lower() for member in group['members'])
    ]
    
    return render_template('search_results.html', query=query, results=results, result_count=len(results))

@app.route('/view/<id>', methods=['GET'])
def view_item(id):
    print("id: ", id)
    for g in groups:
        if g["id"] == id:
            group = g
            break

    similar_group_names = []
    print("group: ", group)
    for similar_id in group["similar groups"]:
        for g in groups:
            if g["id"] == similar_id:
                similar_group = g
                break
        similar_group_names.append({
            "group name": similar_group["group name"],
            "id": similar_group["id"]
        })

    group["similar_group_names"] = similar_group_names

    return render_template('view_group.html', group=group)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Get form data
        received_data = request.get_json()

        group_name = received_data["group_name"]
        image = received_data["image"]
        debut_year = received_data["debut_year"]
        introduction = received_data["introduction"]
        members = received_data["members"]
        discography = received_data["discography"]
        fandom = received_data["fandom"]
        rating = received_data["rating"]
        similar_groups = received_data["similar_groups"]
        recommended_songs = received_data["recommended_songs"]

        # Create new group data
        new_group = {
            "id": str(len(groups) + 1),
            "group name": group_name,
            "image": image,
            "debut year": debut_year,
            "introduction": introduction,
            "members": members,
            "discography": discography,
            "fandom": fandom,
            "similar groups": similar_groups,  # Add selected similar groups
            "recommended songs": recommended_songs,
            "rating": float(rating)
        }

        # Add new group to the groups list
        groups.append(new_group)

        available_groups = [{"id": group['id'], "name": group['group name']} for group in groups]

        return jsonify({'message': 'New item successfully created', 'id': new_group['id']}), 200

    # Fetch available groups to show as options for similar groups
    available_groups = [{"id": group['id'], "name": group['group name']} for group in groups]
    return render_template('add_item.html', available_groups=available_groups)

@app.route('/success/<id>', methods=['GET'])
def success(id):
    # You can fetch the item from your database or the 'groups' list
    new_item = next((item for item in groups if item["id"] == id), None)

    if new_item is None:
        return "Item not found", 404
    
    available_groups = [{"id": group['id'], "name": group['group name']} for group in groups]
    return render_template('success.html', item_id=id, available_groups=available_groups)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_item(id):
    group = None
    for g in groups:
        if g['id'] == id:
            group = g
            break

    if request.method == 'POST':
        # Handle form submission
        received_data = request.get_json()

        # Update the fields with the new values from the form
        group['group name'] = received_data['group_name']
        group['image'] = received_data['image']
        group['debut year'] = received_data['debut_year']
        group['introduction'] = received_data['introduction']
        group['members'] = received_data['members']
        group['discography'] = received_data['discography']
        group['fandom'] = received_data['fandom']
        group['rating'] = float(received_data['rating'])
        group['recommended songs'] = received_data['recommended_songs']
        group['similar groups'] = received_data['similar_groups']

        return jsonify({'message': 'Item updated successfully', 'id': group['id']}), 200

    # If it's a GET request, just return the edit page with pre-populated data
    available_groups = [{"id": group['id'], "name": group['group name']} for group in groups]
    return render_template('edit_item.html', group=group, available_groups=available_groups)

if __name__ == '__main__':
   app.run(debug = True, port=5003)