from extract.scrapper import read_csv

def transform_csv(data):
    selected_columns = data[['name','author_name', 'review_title', 'review_text', 'rating', 'reviewed_at']]
    df_renamed = selected_columns.rename(columns={
        'name': 'company_name',
        'review_title': 'title', 
        'review_text': 'description', 
    })
    return df_renamed


if __name__ == "__main__":
    data = read_csv()
    print(transform_csv(data))

