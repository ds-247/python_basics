import json;


# in below file opening we use try catch  as we want to return something if file is not present 
def load_data() :
    try:
        with open('db.txt') as file:
            # jsong.load -> get all files from file and convert it into json
            return json.load(file)
    except FileNotFoundError :
       return [];


#  but in following file handling as we dont want to return something if file is not present , we are not using trycatch
def save_data_helper (videos) :
    with open('db.txt', 'w') as file :
        # following method is used to writte a file in json formate dump(what_to_write, where_to_write)
        json.dump(videos, file); 

# why to make enumerate -> as it adds index automatically which is use full  for update and delete method
def list_all_videos(videos) :
    print("\n")
    print("*"*73)
    for index, video in enumerate(videos, start = 1) :
        print(f"{index} => Video : {video['name']}   ---   Duration : {video['time']}.");
    print("*"*73)
    print("\n")

#  our data is stored in this way  ->  [{'name', :  "name", 'time' : "time"}, {}]
def add_video(videos):
    name = input("Enter the name of video : ");
    time = input("Enter the duration of video : ");
    videos.append({'name': name, 'time': time});
    save_data_helper(videos);

def update_video(videos) :
    list_all_videos(videos);
    index_of_video = int(input("Please enter the video number you want to update... "));

    if 1 <= index_of_video <= len(videos) :
        name_of_video = input("Please enter the new name you want to update... ");
        time_of_video = input("Please enter the video number you want to update... ");
        videos[index_of_video-1] = {'name': name_of_video, 'time': time_of_video}
        save_data_helper(videos);
    else :
        print("Invalid index selected ...")

def delete_video(videos):
    list_all_videos(videos);
    index_of_video = int(input("Please enter the video number you want to delete... "));
   
    if 1 <= index_of_video <= len(videos) :
            del videos[index_of_video-1]
            save_data_helper(videos);
    else :
        print("Invalid index selected ...")



def main() :
    videos = load_data();

    while 1 :
        print("\n Youtube Video Managing App | Choose an option");
        print("1. List all youtube videos ")
        print("2. Add a youtube video ");
        print("3. Update a youtube video details ");
        print("4. Delete a youtube video ");
        print("5. Exit the app");
        choice = input("Enter your choice : ");
        # print("videos", videos)

        match choice : 
            case '1':
                list_all_videos(videos);
            case '2' :
                add_video(videos);
            case '3' :
                update_video(videos);
            case '4': 
                delete_video(videos);
            case '5' :
                break;
            case _: 
                print("Invalid choice");

if __name__  == '__main__' :
    main();