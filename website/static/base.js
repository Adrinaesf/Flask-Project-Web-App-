function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ noteId: noteId }),
    }).then(() => {
      window.location.reload();
    });
  }
  