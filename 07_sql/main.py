import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        time VARCHAR(50)
    )
''')

def list_all_videos() :
    print("\n")
    print("*"*73)
    cur.execute('''
                 SELECT * FROM videos;
    ''')

    for row in cur.fetchall() :
        print(row);

    print("*"*73)
    print("\n")


def update_video(video_id, name, time) :
    cur.execute("UPDATE  videos SET name = ? , time = ? WHERE id = ?", (name, time, video_id));
    con.commit();

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit() ;

def main() :
    while 1 :
        print("\n Youtube Video Managing App | Choose an option");
        print("1. List all youtube videos ")
        print("2. Add a youtube video ");
        print("3. Update a youtube video details ");
        print("4. Delete a youtube video ");
        print("5. Exit the app");
        choice = input("Enter your choice : ");

        if choice == '1' :
            list_all_videos();
        elif  choice == '2':
            name = input("Enter name of video ... ")
            time = input("Enter the duration of video ... ");
            cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
            con.commit();
        elif choice == '3' :
            video_id = input("enter the video_id : ");
            name = input('enter the new name : ');
            time = input("enter the new duration : ");
            update_video( video_id, name, time);
        elif choice == '4' :
            video_id = input("enter the video id to be deleted  : ")
            delete_video(video_id);
        elif '5':
            break;
        else :
            print("Invalid selection ... ")

    con.close();

if __name__  == '__main__' :
    main();